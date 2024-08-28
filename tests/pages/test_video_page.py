from yt_dlp import YoutubeDL


def test_video_page(client, monkeypatch, video_info):
    def mock_extract_info(*args, **kwargs):
        return video_info

    monkeypatch.setattr(YoutubeDL, "extract_info", mock_extract_info)

    video_id = "dQw4w9WgXcQ"
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"

    response = client.get(f"/{video_id}")
    data = response.data.decode()

    assert "<title>Rick Astley - Never Gonna Give You Up (Official Music Video)</title>" in data
    assert f"<link rel=\"canonical\" href=\"{youtube_url}\" />" in data
    assert f"<meta http-equiv=\"refresh\" content=\"0; url={youtube_url}\" />"
    assert "<meta property=\"og:type\" content=\"video.movie\" />" in data
    assert f"<meta property=\"og:url\" content=\"{youtube_url}\" />" in data
    assert "<meta property=\"og:site_name\" content=\"FixTube\" />" in data

    assert "<meta name=\"description\"" in data
    assert "<meta property=\"og:title\"" in data
    assert "<meta property=\"og:description\"" in data
    assert "<meta property=\"og:image\"" in data
