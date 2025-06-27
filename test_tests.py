import pytest
from fastapi.testclient import TestClient # type: ignore
from main import app
from unittest.mock import patch
from sqlalchemy.exc import OperationalError
from sqlalchemy import text
from DATABASE.dbConnection import SessionLocal



@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def valid_token():
    return "valid_test_token"

def test_Root_Returns_Hello_World(client):
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
    
def test_protected_route_no_token(client):
    response = client.get("/health/protected")
    assert response.status_code == 401

def test_protected_route_with_valid_token(client, valid_token):
    with patch("firebase_admin.auth.verify_id_token") as mock_verify:
        mock_verify.return_value = {"uid": "test_user"}
        response = client.get("/health/protected", headers={"Authorization": f"Bearer {valid_token}"})
        assert response.status_code == 200
         # adjust to your actual response
         
def test_create_user(client):
    with patch("firebase_admin.auth.verify_id_token") as mock_verify:
        mock_verify.return_value = {"uid": "test_user"}

        response = client.post(
            "/users/createUser",
            headers={"Authorization": f"Bearer {valid_token}"},
            json={
                "UserId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "Email": "user@example.com",
                "FirstName": "string",
                "LastName": "string",
                "DateOfBirth": "2025-06-27",
                "TimeOfLastLogin": "2025-06-27T19:13:54.143Z"
            }
        )

        assert response.status_code == 200
        assert response.json()["message"] == "User created"
    
def test_create_user_invalid_email(client):
    with patch("firebase_admin.auth.verify_id_token") as mock_verify:
        mock_verify.return_value = {"uid": "test_user"}

        response = client.post(
            "/users/createUser",
            headers={"Authorization": f"Bearer {valid_token}"},
            json={
                "UserId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "Email": "user@example",
                "FirstName": "string",
                "LastName": "string",
                "DateOfBirth": "2025-06-27",
                "TimeOfLastLogin": "2025-06-27T19:13:54.143Z"
            }
        )

        assert response.status_code == 422

def test_direct_database_connection():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()
        assert True
    except OperationalError as e:
        pytest.fail(f"Database connection failed: {e}")
        
#def test_create_user_success(client, valid_token):
    with patch("firebase_admin.auth.verify_id_token") as mock_verify:
        mock_verify.return_value = {"uid": "test_user"}

        response = client.post(
            "/users/createUser",
            headers={"Authorization": f"Bearer {valid_token}"},
            json={
                "UserId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "Email": "user@example.com",
                "FirstName": "Test",
                "LastName": "User",
                "DateOfBirth": "2000-01-01",
                "TimeOfLastLogin": "2025-06-27T19:13:54.143Z"
            }
        )

        assert response.status_code == 200
        assert response.json()["message"] == "User created"
        
def test_get_existing_user(client):
    # Replace this with the actual UserId of a user already in your database
    existing_user_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6"

    response = client.get(f"/users/getUser/{existing_user_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["UserId"] == existing_user_id