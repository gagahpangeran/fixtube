from yt_dlp import YoutubeDL


def test_server_error_page(client, monkeypatch):
    def mock_extract_info(*args, **kwargs):
        raise Exception()

    monkeypatch.setattr(YoutubeDL, "extract_info", mock_extract_info)

    response = client.get("/servererror")
    data = response.data.decode()

    assert response.status_code == 500
    assert "<title>Internal Server Error</title>" in data
    assert "<meta name=\"description\" content=\"There is something wrong.\" />" in data
    assert "<meta property=\"og:title\" content=\"Internal Server Error\" />" in data
    assert "<meta property=\"og:description\" content=\"There is something wrong.\" />" in data
    assert "<meta property=\"og:site_name\" content=\"FixTube\" />" in data
    assert "<meta property=\"og:type\" content=\"website\" />" in data
    assert "<meta property=\"og:image\" content=\"/static/fixtube.png\" />" in data

    assert "<link rel=\"canonical\" />" not in data
    assert "<meta http-equiv=\"refresh\"" not in data

    assert "<meta property=\"og:video\"" not in data
    assert "<meta property=\"og:video:secure_url\"" not in data
    assert "<meta property=\"og:video:type\"" not in data
    assert "<meta property=\"og:video:width\"" not in data
    assert "<meta property=\"og:video:height\"" not in data
