import pytest
from sample_app import sample


@pytest.fixture
def client():
    sample.config["TESTING"] = True

    with sample.test_client() as client:
        yield client


def test_pagina_principal(client):
    respuesta = client.get("/")

    assert respuesta.status_code == 200
    assert b"Bienvenido a mi aplicacion Flask" in respuesta.data

