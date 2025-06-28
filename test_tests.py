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

def test_direct_database_connection(client):
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()
        assert True
    except OperationalError as e:
        pytest.fail(f"Database connection failed: {e}")
        
def test_create_user_success(client, valid_token):
    with patch("firebase_admin.auth.verify_id_token") as mock_verify:
        mock_verify.return_value = {"uid": "test_user"}

        response = client.post(
            "/users/createUser",
            headers={"Authorization": f"Bearer {valid_token}"},
            json={
                "UserId": "4fa85f64-5717-4562-b3fc-2c963f66afa6",
                "Email": "user@example.com",
                "FirstName": "Test",
                "LastName": "User",
                "DateOfBirth": "2000-01-01",
                "TimeOfLastLogin": "2025-06-27T19:13:54.143Z"
            }
        )
        
        data = response.json()

        assert response.status_code == 200
        assert data["UserId"] == "4fa85f64-5717-4562-b3fc-2c963f66afa6"
        
def test_get_existing_user(client):
    # Replace this with the actual UserId of a user already in your database
    existing_user_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6"

    response = client.get(f"/users/getUser/{existing_user_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["UserId"] == existing_user_id
    
def test_update_user_last_login(client):
    # Replace with an actual existing UserId in your test DB
    existing_user_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    
    response = client.put(f"/users/updateUserLastLogin/{existing_user_id}")

    assert response.status_code == 200
    data = response.json()
    
    assert data["UserId"] == existing_user_id
    assert "TimeOfLastLogin" in data
    assert data["TimeOfLastLogin"] is not None
    
def test_delete_user(client):
    # Replace with an actual existing UserId in your test DB
    user_id_to_delete = "4fa85f64-5717-4562-b3fc-2c963f66afa6"
    
    response = client.delete(f"/users/deleteUser/{user_id_to_delete}")
    
    assert response.status_code == 200
    assert response.json()["UserId"] == user_id_to_delete
    
    

def test_create_location(client):
    payload = {
        "LocationId": 2,
        "LocationName": "Downtown2 Park"
    }

    response = client.post("/locations/createLocation", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "LocationId" in data
    assert data["LocationName"] == "Downtown2 Park"
    
    
    
def test_get_existing_location(client):
    # Use a LocationId that you know exists in the database
    existing_location_id = 1

    response = client.get(f"/locations/getLocation/{existing_location_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["LocationId"] == existing_location_id
    assert "LocationName" in data
    
    
def test_get_all_locations(client):
    response = client.get("/locations/allLocations")  # adjust path if you use a prefix
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
    # Optional: if you expect at least one location already in the DB
    if response.json():
        location = response.json()[0]
        assert "LocationId" in location
        assert "LocationName" in location
        
def test_update_location(client):
    location_id_to_update = 1
    new_location_name = "Updated Park"

    response = client.put(
        f"/locations/updateLocation/{location_id_to_update}",
        json={"LocationId": location_id_to_update, "LocationName": new_location_name}
    )

    assert response.status_code == 200
    data = response.json()
    assert data["LocationId"] == location_id_to_update
    assert data["LocationName"] == new_location_name
    
def test_delete_location(client):
    location_id_to_delete = 2
    
    response = client.delete(f"/locations/deleteLocation/{location_id_to_delete}")
    
    assert response.status_code == 200
    assert response.json()["LocationId"] == location_id_to_delete


def test_create_bar(client):
    payload = {
        "BarId": "123e4567-e89b-12d3-a456-426614174000",
        "LocationId": 1,
        "BarName": "Test Bar"
    }

    response = client.post("/bars/createBar", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert data["BarId"] == payload["BarId"]
    assert data["LocationId"] == payload["LocationId"]
    assert data["BarName"] == payload["BarName"]
    