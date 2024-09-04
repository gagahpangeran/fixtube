def test_index_page(client):
    response = client.get("/")
    data = response.data.decode()

    assert "<title>FixTube</title>" in data
    assert "<meta name=\"description\" content=\"Fix your youtube embed.\" />" in data
    assert "<link rel=\"canonical\" href=\"https://www.youtube.com\" />" in data
    assert "<meta http-equiv=\"refresh\" content=\"0; url=https://www.youtube.com\" />"
    assert "<meta property=\"og:title\" content=\"FixTube\" />" in data
    assert "<meta property=\"og:description\" content=\"Fix your youtube embed.\" />" in data
    assert "<meta property=\"og:site_name\" content=\"FixTube\" />" in data
    assert "<meta property=\"og:type\" content=\"website\" />" in data
    assert "<meta property=\"og:image\" content=\"/static/fixtube.png\" />" in data

    assert "<meta property=\"og:video\"" not in data
    assert "<meta property=\"og:video:secure_url\"" not in data
    assert "<meta property=\"og:video:type\"" not in data
    assert "<meta property=\"og:video:width\"" not in data
    assert "<meta property=\"og:video:height\"" not in data
