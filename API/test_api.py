import pytest
from fastapi.testclient import TestClient # type: ignore
from main import app
from unittest.mock import patch




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
        