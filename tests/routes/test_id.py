import pytest
from yt_dlp import YoutubeDL
from yt_dlp.utils import YoutubeDLError


@pytest.mark.skip(reason="Currently disabled")
def test_id_valid_id(client, monkeypatch, video_info):
    def mock_extract_info(*args, **kwargs):
        return video_info

    monkeypatch.setattr(YoutubeDL, "extract_info", mock_extract_info)

    response = client.get("/dQw4w9WgXcQ")
    assert response.status_code == 200


@pytest.mark.skip(reason="Currently disabled")
def test_id_empty_id(client):
    response = client.get("/  ")
    assert response.status_code == 404


@pytest.mark.skip(reason="Currently disabled")
def test_id_invalid_id(client, monkeypatch):
    def mock_extract_info(*args, **kwargs):
        raise YoutubeDLError("video not found")

    monkeypatch.setattr(YoutubeDL, "extract_info", mock_extract_info)

    response = client.get("/randomvideo")
    assert response.status_code == 404
