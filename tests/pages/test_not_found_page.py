def test_index_page(client):
    response = client.get("/ok/")
    data = response.data.decode()

    assert response.status_code == 404
    assert "<title>Video not found</title>" in data
    assert "<meta name=\"description\" content=\"404 not found.\" />" in data
    assert "<link rel=\"canonical\" href=\"https://www.youtube.com\" />" in data
    assert "<meta http-equiv=\"refresh\" content=\"0; url=https://www.youtube.com\" />"
    assert "<meta property=\"og:title\" content=\"Video not found\" />" in data
    assert "<meta property=\"og:description\" content=\"404 not found.\" />" in data
    assert "<meta property=\"og:site_name\" content=\"FixTube\" />" in data
    assert "<meta property=\"og:type\" content=\"website\" />" in data
    assert "<meta property=\"og:image\" content=\"/static/fixtube.png\" />" in data
    assert "<meta property=\"og:video\"" not in data
