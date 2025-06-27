import pytest
from fastapi.testclient import TestClient # type: ignore
from ApiEndpoint import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def valid_token():
    # You can replace this with actual token generation logic
    return "valid_test_token"

def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
    
def test_protected_route_no_token(client):
    response = client.get("/protected")
    assert response.status_code == 401

def test_protected_route_with_valid_token(client, valid_token):
    response = client.get("/protected", headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200