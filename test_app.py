import pytest
from sample_app import sample


@pytest.fixture
def client():
    sample.config["TESTING"] = True

    with sample.test_client() as client:
        yield client


def test_api_status(client):
    response = client.get("/")

    assert response.status_code == 200


def test_api_content_type(client):
    response = client.get("/")

    assert response.content_type.startswith("text/html")


def test_api_contains_title(client):
    response = client.get("/")

    assert b"Bienvenido a mi aplicacion Flask" in response.data
