import pytest
from fastapi.testclient import TestClient
from main import app, users

@pytest.fixture
def client():
    users.clear()
    return TestClient(app)