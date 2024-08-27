from fixtube.utils import get_ytdl_info


def test_get_ytdl_info_valid_id():
    video_id = "dQw4w9WgXcQ"
    info = get_ytdl_info(video_id)

    assert "id" in info
    assert info["id"] == video_id

    assert "title" in info
    assert "formats" in info


def test_get_ytdl_info_not_found_id():
    video_id = "randomvideo"
    info = get_ytdl_info(video_id)

    assert info is None


def test_get_ytdl_info_invalid_id():
    video_id = "abc"
    info = get_ytdl_info(video_id)

    assert info is None
