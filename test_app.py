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


def test_database_connection(client):
    response = client.get("/")

    assert b"Conexion exitosa a la base de datos" in response.data
