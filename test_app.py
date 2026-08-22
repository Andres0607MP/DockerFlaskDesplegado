import pytest
from sample_app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_api_status(client):
    response = client.get("/")

    assert response.status_code == 200


def test_api_returns_json(client):
    response = client.get("/")

    assert response.content_type == "application/json"


def test_api_has_data(client):
    response = client.get("/")

    data = response.get_json()

    assert data is not None
