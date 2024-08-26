from flask.testing import FlaskClient


def test_index(client: FlaskClient):
    response = client.get("/")
    assert response.data == b"Hello!"
