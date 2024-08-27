import pytest
from flask import Flask
from fixtube import create_app
from fixtures.scripts import get_fixture_video_info


@pytest.fixture()
def app():
    app = create_app()

    yield app


@pytest.fixture()
def client(app: Flask):
    return app.test_client()


@pytest.fixture()
def runner(app: Flask):
    return app.test_cli_runner()


@pytest.fixture()
def video_info():
    return get_fixture_video_info()
