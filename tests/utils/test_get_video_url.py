from fixtube.utils import get_best_format

VALID_VIDEO_URL = "https://rr4---sn-jcopn2-jb3s.googlevideo.com/videoplayback?expire=1724719916&ei=y87MZp2BPc68rtoP47XTaQ&ip=103.121.136.234&id=o-AHj4cSbFpV0LO66ixetz68Q5Fa7w0ySdqpZQQyXMwqmN&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=7c&mm=31%2C29&mn=sn-jcopn2-jb3s%2Csn-npoe7nsl&ms=au%2Crdu&mv=m&mvi=4&pl=24&initcwndbps=795000&bui=AQmm2eyMkC8VZencnSWw6baeJ0ZM6T-weuEYt1CxWReq8UKbBdXgrv_PiGp9jHsKy0cOhhyjnRRp6beX&spc=Mv1m9voCQ-oe4LoVl1nIo8xQ9o3xo3w3R7j8o3RN7GY6Yj8bsxQ2BhI&vprv=1&svpuc=1&mime=video%2Fmp4&ns=V1sCFsSoMBka1eh7SlHwqhEQ&rqh=1&cnr=14&ratebypass=yes&dur=212.091&lmt=1717051812678016&mt=1724697905&fvip=2&c=WEB_CREATOR&sefc=1&txp=4538434&n=HLI4LC0nk972Ug&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Ccnr%2Cratebypass%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AGtxev0wRQIgfiqF6uyHoT14NsPQ9l-_KO1Vhu9G6TBX4-ieD-_eQ4cCIQCTVUCGWGitMOa2bx5xlw_U-MHEnqxYVejgGuJNLFD5hw%3D%3D&sig=AJfQdSswRAIgbmiR_2_QY2-S9vtpVRpJcqlgCITd7rSrYQdaEkVElTsCIHQaxxDriBS7eozB82VHCLFewkQRqFBDPIZyTNGpJLWy"


def test_get_best_format(video_info):
    format = get_best_format(video_info["formats"])
    assert format["url"] == VALID_VIDEO_URL
    assert format["ext"] == "mp4"
    assert format["width"] == 640
    assert format["height"] == 360


def test_get_best_format_no_vcodec(video_info):
    formats = video_info["formats"]
    for format in formats:
        if "vcodec" in format:
            format["vcodec"] = "none"

    format = get_best_format(formats)
    assert format is None


def test_get_best_format_no_acodec(video_info):
    formats = video_info["formats"]
    for format in formats:
        if "acodec" in format:
            format["acodec"] = "none"

    format = get_best_format(formats)
    assert format is None
