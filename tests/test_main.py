import pytest
from fastapi.testclient import TestClient

from foo_bar_banana import app


@pytest.fixture
def client():
    return TestClient(app)


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "World" in response.json().get("Hello", "")
