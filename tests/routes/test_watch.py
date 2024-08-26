from flask.testing import FlaskClient


def test_watch_id(client: FlaskClient):
    response = client.get("/watch?v=abcd")
    assert response.data == b"abcd"


def test_watch_id_empty(client: FlaskClient):
    response = client.get("/watch?v=")
    assert response.status_code == 404


def test_watch_no_id(client: FlaskClient):
    response = client.get("/watch")
    assert response.status_code == 404
