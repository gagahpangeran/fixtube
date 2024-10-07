from yt_dlp import YoutubeDL


def test_video_page(client, monkeypatch, video_info):
    def mock_extract_info(*args, **kwargs):
        return video_info

    monkeypatch.setattr(YoutubeDL, "extract_info", mock_extract_info)

    video_id = "dQw4w9WgXcQ"
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"
    video_url = "https://rr2---sn-npoeenll.googlevideo.com/videoplayback?expire=1728253273&ei=-bgCZ_GvJeS7rtoPl5uIkQ8&ip=129.227.46.149&id=o-AAN7scGLA3prwRahnWRR_JdSHbr-smqnDez-Jfxr8WGV&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=7c&mm=31%2C26&mn=sn-npoeenll%2Csn-30a7ynek&ms=au%2Conr&mv=m&mvi=2&pl=23&initcwndbps=518750&bui=AXLXGFQWnTs4-F6uA4b9wVFYGx2hPuHPB7oS8AkPbYSLVZBGEtx4m_JDGOelC4YIzCvqzPJfDbySjm-A&spc=54MbxW3SkS-5NtFFSKuQYStzrMEEf4qTAl55H_K6ZBfZH9gy-YXJ&vprv=1&svpuc=1&mime=video%2Fmp4&ns=BukalNEnTlobLD8bwXxyfvMQ&rqh=1&cnr=14&ratebypass=yes&dur=212.091&lmt=1717051812678016&mt=1728231207&fvip=2&fexp=51300761&c=WEB_CREATOR&sefc=1&txp=4538434&n=NBhUCs17_lPniw&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Ccnr%2Cratebypass%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=ACJ0pHgwRAIgWDEpCcAZK-qZbDlgFPNLUYBAd_YjIraWOinINS8H_qICIEBP9554Ns-b9lfDchh9pQM08YCLuKNUuGLak8E-kEMH&sig=AJfQdSswRQIhAO9v2fZkzZ0VXDO8r0GidoRFWPuvXsheg4QYFNJS3PZmAiBsMhvF2JU9Rt__pwC49VzQworCl1ybiNWLd2x1ecLqcA%3D%3D"

    response = client.get(f"/watch?v={video_id}")
    data = response.data.decode()

    assert "<title>Rick Astley - Never Gonna Give You Up (Official Music Video)</title>" in data
    assert f"<link rel=\"canonical\" href=\"{youtube_url}\" />" in data
    assert f"<meta http-equiv=\"refresh\" content=\"0; url={youtube_url}\" />"
    assert "<meta property=\"og:type\" content=\"video.movie\" />" in data
    assert f"<meta property=\"og:url\" content=\"{youtube_url}\" />" in data
    assert "<meta property=\"og:site_name\" content=\"FixTube\" />" in data
    assert f"<meta property=\"og:video\" content=\"{video_url}\" />" in data

    assert "<meta name=\"description\"" in data
    assert "<meta property=\"og:title\"" in data
    assert "<meta property=\"og:description\"" in data
    assert "<meta property=\"og:image\"" in data
    assert "<meta property=\"og:video:secure_url\"" in data
    assert "<meta property=\"og:video:type\"" in data
    assert "<meta property=\"og:video:width\"" in data
    assert "<meta property=\"og:video:height\"" in data
