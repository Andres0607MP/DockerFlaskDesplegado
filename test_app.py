import pytest
from sample_app import sample


@pytest.fixture
def client():
    sample.config["TESTING"] = True

    with sample.test_client() as client:
        yield client


def test_error_conexion_bd(client):
    respuesta = client.get("/")

    assert respuesta.status_code == 200
    assert b"Error al conectar a la base de datos" in respuesta.data

