from flask.testing import FlaskClient


def test_live_id(client: FlaskClient):
    response = client.get("/live/abcd")
    assert response.data == b"abcd"


def test_live_id_empty(client: FlaskClient):
    response = client.get("/live/  ")
    assert response.status_code == 404


def test_live_no_id(client: FlaskClient):
    response = client.get("/live/")
    assert response.status_code == 404
