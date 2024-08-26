from flask.testing import FlaskClient


def test_id(client: FlaskClient):
    response = client.get("/abcd")
    assert response.data == b"abcd"


def test_id_empty(client: FlaskClient):
    response = client.get("/  ")
    assert response.status_code == 404
