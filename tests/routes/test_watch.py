from yt_dlp import YoutubeDL
from yt_dlp.utils import YoutubeDLError


def test_watch_id(client, monkeypatch, video_info):
    def mock_extract_info(*args, **kwargs):
        return video_info

    monkeypatch.setattr(YoutubeDL, "extract_info", mock_extract_info)

    response = client.get("/watch?v=dQw4w9WgXcQ")
    assert response.status_code == 200


def test_watch_empty_id(client):
    response = client.get("/watch?v=")
    assert response.status_code == 404


def test_watch_no_id(client):
    response = client.get("/watch")
    assert response.status_code == 404


def test_watch_invalid_id(client, monkeypatch):
    def mock_extract_info(*args, **kwargs):
        raise YoutubeDLError("video not found")

    monkeypatch.setattr(YoutubeDL, "extract_info", mock_extract_info)

    response = client.get("/randomvideo")
    assert response.status_code == 404
