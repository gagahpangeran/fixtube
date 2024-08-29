from yt_dlp import YoutubeDL
from yt_dlp.utils import YoutubeDLError
from fixtube.utils import get_ytdl_info


def test_get_ytdl_info_valid_url(monkeypatch, video_info):
    def mock_extract_info(*args, **kwargs):
        return video_info

    monkeypatch.setattr(YoutubeDL, "extract_info", mock_extract_info)

    video_id = "dQw4w9WgXcQ"
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"
    info = get_ytdl_info(youtube_url)

    assert "id" in info
    assert info["id"] == video_id

    assert "title" in info
    assert "formats" in info

    assert "live_status" in info
    assert info["live_status"] != "is_live"


def test_get_ytdl_info_valid_live_url(monkeypatch, live_video_info):
    def mock_extract_info(*args, **kwargs):
        return live_video_info

    monkeypatch.setattr(YoutubeDL, "extract_info", mock_extract_info)

    video_id = "NlBLeMiRKT4"
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"
    info = get_ytdl_info(youtube_url)

    assert "id" in info
    assert info["id"] == video_id

    assert "title" in info
    assert "formats" in info

    assert "live_status" in info
    assert info["live_status"] == "is_live"


def test_get_ytdl_info_invalid_url(monkeypatch, video_info):
    def mock_extract_info(*args, **kwargs):
        raise YoutubeDLError("video not found")

    monkeypatch.setattr(YoutubeDL, "extract_info", mock_extract_info)

    youtube_url = "https://www.youtube.com/watch?v=randomvideo"
    info = get_ytdl_info(youtube_url)

    assert info is None
