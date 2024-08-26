from flask.testing import FlaskClient


def test_shorts_id(client: FlaskClient):
    response = client.get("/shorts/abcd")
    assert response.data == b"abcd"


def test_shorts_id_empty(client: FlaskClient):
    response = client.get("/shorts/  ")
    assert response.status_code == 404


def test_shorts_no_id(client: FlaskClient):
    response = client.get("/shorts/")
    assert response.status_code == 404
