import pytest
from fastapi.testclient import TestClient # type: ignore
from Appz.API.main import app
from unittest.mock import patch
import sys
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parents[2]))

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def valid_token():
    return "valid_test_token"

def test_Root_Returns_Hello_World(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
    
def test_protected_route_no_token(client):
    response = client.get("/protected")
    assert response.status_code == 401

def test_protected_route_with_valid_token(client, valid_token):
    with patch("firebase_admin.auth.verify_id_token") as mock_verify:
        mock_verify.return_value = {"uid": "test_user"}
        response = client.get("/protected", headers={"Authorization": f"Bearer {valid_token}"})
        assert response.status_code == 200
         # adjust to your actual response