from yt_dlp import YoutubeDL


def test_video_page(client, monkeypatch, live_video_info):
    def mock_extract_info(*args, **kwargs):
        return live_video_info

    monkeypatch.setattr(YoutubeDL, "extract_info", mock_extract_info)

    video_id = "NlBLeMiRKT4"
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"

    response = client.get(f"/live/{video_id}")
    data = response.data.decode()

    assert "<title>Live High-Definition Views from the International Space Station (Official NASA Stream) 2024-08-27 01:56</title>" in data
    assert f"<link rel=\"canonical\" href=\"{youtube_url}\" />" in data
    assert f"<meta http-equiv=\"refresh\" content=\"0; url={youtube_url}\" />"
    assert "<meta property=\"og:type\" content=\"website\" />" in data
    assert f"<meta property=\"og:url\" content=\"{youtube_url}\" />" in data
    assert "<meta property=\"og:site_name\" content=\"FixTube\" />" in data

    assert "<meta name=\"description\"" in data
    assert "<meta property=\"og:title\"" in data
    assert "<meta property=\"og:description\"" in data
    assert "<meta property=\"og:image\"" in data

    assert "<meta property=\"og:video\"" not in data
