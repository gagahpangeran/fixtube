from yt_dlp import YoutubeDL
from yt_dlp.utils import YoutubeDLError
from fixtube.utils import get_ytdl_info


def test_get_ytdl_info_valid_id(monkeypatch, video_info):
    def mock_extract_info(*args, **kwargs):
        return video_info

    monkeypatch.setattr(YoutubeDL, "extract_info", mock_extract_info)

    video_id = "dQw4w9WgXcQ"
    info = get_ytdl_info(video_id)

    assert "id" in info
    assert info["id"] == video_id

    assert "title" in info
    assert "formats" in info


def test_get_ytdl_info_not_found_id(monkeypatch, video_info):
    def mock_extract_info(*args, **kwargs):
        raise YoutubeDLError("video not found")

    monkeypatch.setattr(YoutubeDL, "extract_info", mock_extract_info)

    video_id = "randomvideo"
    info = get_ytdl_info(video_id)

    assert info is None
