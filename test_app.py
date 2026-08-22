import requests

BASE_URL = "http://localhost:5050"


def test_api_status():
    response = requests.get(f"{BASE_URL}/")

    assert response.status_code == 200


def test_api_response():
    response = requests.get(f"{BASE_URL}/")

    assert response.headers["Content-Type"].startswith("application/json")


def test_api_has_data():
    response = requests.get(f"{BASE_URL}/")

    data = response.json()

    assert data is not None
    assert len(data) > 0
