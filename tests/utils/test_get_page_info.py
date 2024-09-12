from yt_dlp import YoutubeDL
from yt_dlp.utils import YoutubeDLError
from fixtube.utils import get_page_info


def test_get_page_info_valid_id(monkeypatch, video_info):
    def mock_extract_info(*args, **kwargs):
        return video_info

    monkeypatch.setattr(YoutubeDL, "extract_info", mock_extract_info)

    video_id = "dQw4w9WgXcQ"
    page_info = get_page_info(video_id)

    expected_info = {
        "title": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
        "description": "The official video for \u201cNever Gonna Give You Up\u201d by Rick Astley. \n\nThe new album 'Are We There Yet?' is out now: Download here: https://RickAstley.lnk.to/AreWeThereYetFA/itunes\n\n\u201cNever Gonna Give You Up\u201d was a global smash on its release in July 1987, topping the charts in 25 countries including Rick\u2019s native UK and the US Billboard Hot 100.  It also won the Brit Award for Best single in 1988. Stock Aitken and Waterman wrote and produced the track which was the lead-off single and lead track from Rick\u2019s debut LP \u201cWhenever You Need Somebody\u201d.  The album was itself a UK number one and would go on to sell over 15 million copies worldwide.\n\nThe legendary video was directed by Simon West \u2013 who later went on to make Hollywood blockbusters such as Con Air, Lara Croft \u2013 Tomb Raider and The Expendables 2.  The video passed the 1bn YouTube views milestone on 28 July 2021.\n\nSubscribe to the official Rick Astley YouTube channel: https://RickAstley.lnk.to/YTSubID\n\nFollow Rick Astley:\nFacebook: https://RickAstley.lnk.to/FBFollowID \nTwitter: https://RickAstley.lnk.to/TwitterID \nInstagram: https://RickAstley.lnk.to/InstagramID \nWebsite: https://RickAstley.lnk.to/storeID \nTikTok: https://RickAstley.lnk.to/TikTokID\n\nListen to Rick Astley:\nSpotify: https://RickAstley.lnk.to/SpotifyID \nApple Music: https://RickAstley.lnk.to/AppleMusicID \nAmazon Music: https://RickAstley.lnk.to/AmazonMusicID \nDeezer: https://RickAstley.lnk.to/DeezerID \n\nLyrics:\nWe\u2019re no strangers to love\nYou know the rules and so do I\nA full commitment\u2019s what I\u2019m thinking of\nYou wouldn\u2019t get this from any other guy\n\nI just wanna tell you how I\u2019m feeling\nGotta make you understand\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\nWe\u2019ve known each other for so long\nYour heart\u2019s been aching but you\u2019re too shy to say it\nInside we both know what\u2019s been going on\nWe know the game and we\u2019re gonna play it\n\nAnd if you ask me how I\u2019m feeling\nDon\u2019t tell me you\u2019re too blind to see\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\n#RickAstley #NeverGonnaGiveYouUp #WheneverYouNeedSomebody #OfficialMusicVideo",
        "original_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "tw_info": {
            "twitter:card": "player",
            "twitter:title": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
            "twitter:player:width": 640,
            "twitter:player:height": 360,
            "twitter:player:stream": "https://rr4---sn-jcopn2-jb3s.googlevideo.com/videoplayback?expire=1724719916&ei=y87MZp2BPc68rtoP47XTaQ&ip=103.121.136.234&id=o-AHj4cSbFpV0LO66ixetz68Q5Fa7w0ySdqpZQQyXMwqmN&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=7c&mm=31%2C29&mn=sn-jcopn2-jb3s%2Csn-npoe7nsl&ms=au%2Crdu&mv=m&mvi=4&pl=24&initcwndbps=795000&bui=AQmm2eyMkC8VZencnSWw6baeJ0ZM6T-weuEYt1CxWReq8UKbBdXgrv_PiGp9jHsKy0cOhhyjnRRp6beX&spc=Mv1m9voCQ-oe4LoVl1nIo8xQ9o3xo3w3R7j8o3RN7GY6Yj8bsxQ2BhI&vprv=1&svpuc=1&mime=video%2Fmp4&ns=V1sCFsSoMBka1eh7SlHwqhEQ&rqh=1&cnr=14&ratebypass=yes&dur=212.091&lmt=1717051812678016&mt=1724697905&fvip=2&c=WEB_CREATOR&sefc=1&txp=4538434&n=HLI4LC0nk972Ug&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Ccnr%2Cratebypass%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AGtxev0wRQIgfiqF6uyHoT14NsPQ9l-_KO1Vhu9G6TBX4-ieD-_eQ4cCIQCTVUCGWGitMOa2bx5xlw_U-MHEnqxYVejgGuJNLFD5hw%3D%3D&sig=AJfQdSswRAIgbmiR_2_QY2-S9vtpVRpJcqlgCITd7rSrYQdaEkVElTsCIHQaxxDriBS7eozB82VHCLFewkQRqFBDPIZyTNGpJLWy",
            "twitter:player:stream:content_type": "video/mp4",
        },
        "og_info": {
            "og:title": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
            "og:description": "The official video for \u201cNever Gonna Give You Up\u201d by Rick Astley. \n\nThe new album 'Are We There Yet?' is out now: Download here: https://RickAstley.lnk.to/AreWeThereYetFA/itunes\n\n\u201cNever Gonna Give You Up\u201d was a global smash on its release in July 1987, topping the charts in 25 countries including Rick\u2019s native UK and the US Billboard Hot 100.  It also won the Brit Award for Best single in 1988. Stock Aitken and Waterman wrote and produced the track which was the lead-off single and lead track from Rick\u2019s debut LP \u201cWhenever You Need Somebody\u201d.  The album was itself a UK number one and would go on to sell over 15 million copies worldwide.\n\nThe legendary video was directed by Simon West \u2013 who later went on to make Hollywood blockbusters such as Con Air, Lara Croft \u2013 Tomb Raider and The Expendables 2.  The video passed the 1bn YouTube views milestone on 28 July 2021.\n\nSubscribe to the official Rick Astley YouTube channel: https://RickAstley.lnk.to/YTSubID\n\nFollow Rick Astley:\nFacebook: https://RickAstley.lnk.to/FBFollowID \nTwitter: https://RickAstley.lnk.to/TwitterID \nInstagram: https://RickAstley.lnk.to/InstagramID \nWebsite: https://RickAstley.lnk.to/storeID \nTikTok: https://RickAstley.lnk.to/TikTokID\n\nListen to Rick Astley:\nSpotify: https://RickAstley.lnk.to/SpotifyID \nApple Music: https://RickAstley.lnk.to/AppleMusicID \nAmazon Music: https://RickAstley.lnk.to/AmazonMusicID \nDeezer: https://RickAstley.lnk.to/DeezerID \n\nLyrics:\nWe\u2019re no strangers to love\nYou know the rules and so do I\nA full commitment\u2019s what I\u2019m thinking of\nYou wouldn\u2019t get this from any other guy\n\nI just wanna tell you how I\u2019m feeling\nGotta make you understand\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\nWe\u2019ve known each other for so long\nYour heart\u2019s been aching but you\u2019re too shy to say it\nInside we both know what\u2019s been going on\nWe know the game and we\u2019re gonna play it\n\nAnd if you ask me how I\u2019m feeling\nDon\u2019t tell me you\u2019re too blind to see\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\n#RickAstley #NeverGonnaGiveYouUp #WheneverYouNeedSomebody #OfficialMusicVideo",
            "og:type": "video.movie",
            "og:image": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/maxresdefault.webp",
            "og:url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "og:site_name": "FixTube",
            "og:video": "https://rr4---sn-jcopn2-jb3s.googlevideo.com/videoplayback?expire=1724719916&ei=y87MZp2BPc68rtoP47XTaQ&ip=103.121.136.234&id=o-AHj4cSbFpV0LO66ixetz68Q5Fa7w0ySdqpZQQyXMwqmN&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=7c&mm=31%2C29&mn=sn-jcopn2-jb3s%2Csn-npoe7nsl&ms=au%2Crdu&mv=m&mvi=4&pl=24&initcwndbps=795000&bui=AQmm2eyMkC8VZencnSWw6baeJ0ZM6T-weuEYt1CxWReq8UKbBdXgrv_PiGp9jHsKy0cOhhyjnRRp6beX&spc=Mv1m9voCQ-oe4LoVl1nIo8xQ9o3xo3w3R7j8o3RN7GY6Yj8bsxQ2BhI&vprv=1&svpuc=1&mime=video%2Fmp4&ns=V1sCFsSoMBka1eh7SlHwqhEQ&rqh=1&cnr=14&ratebypass=yes&dur=212.091&lmt=1717051812678016&mt=1724697905&fvip=2&c=WEB_CREATOR&sefc=1&txp=4538434&n=HLI4LC0nk972Ug&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Ccnr%2Cratebypass%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AGtxev0wRQIgfiqF6uyHoT14NsPQ9l-_KO1Vhu9G6TBX4-ieD-_eQ4cCIQCTVUCGWGitMOa2bx5xlw_U-MHEnqxYVejgGuJNLFD5hw%3D%3D&sig=AJfQdSswRAIgbmiR_2_QY2-S9vtpVRpJcqlgCITd7rSrYQdaEkVElTsCIHQaxxDriBS7eozB82VHCLFewkQRqFBDPIZyTNGpJLWy",
            "og:video:secure_url": "https://rr4---sn-jcopn2-jb3s.googlevideo.com/videoplayback?expire=1724719916&ei=y87MZp2BPc68rtoP47XTaQ&ip=103.121.136.234&id=o-AHj4cSbFpV0LO66ixetz68Q5Fa7w0ySdqpZQQyXMwqmN&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=7c&mm=31%2C29&mn=sn-jcopn2-jb3s%2Csn-npoe7nsl&ms=au%2Crdu&mv=m&mvi=4&pl=24&initcwndbps=795000&bui=AQmm2eyMkC8VZencnSWw6baeJ0ZM6T-weuEYt1CxWReq8UKbBdXgrv_PiGp9jHsKy0cOhhyjnRRp6beX&spc=Mv1m9voCQ-oe4LoVl1nIo8xQ9o3xo3w3R7j8o3RN7GY6Yj8bsxQ2BhI&vprv=1&svpuc=1&mime=video%2Fmp4&ns=V1sCFsSoMBka1eh7SlHwqhEQ&rqh=1&cnr=14&ratebypass=yes&dur=212.091&lmt=1717051812678016&mt=1724697905&fvip=2&c=WEB_CREATOR&sefc=1&txp=4538434&n=HLI4LC0nk972Ug&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Ccnr%2Cratebypass%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AGtxev0wRQIgfiqF6uyHoT14NsPQ9l-_KO1Vhu9G6TBX4-ieD-_eQ4cCIQCTVUCGWGitMOa2bx5xlw_U-MHEnqxYVejgGuJNLFD5hw%3D%3D&sig=AJfQdSswRAIgbmiR_2_QY2-S9vtpVRpJcqlgCITd7rSrYQdaEkVElTsCIHQaxxDriBS7eozB82VHCLFewkQRqFBDPIZyTNGpJLWy",
            "og:video:type": "video/mp4",
            "og:video:width": 640,
            "og:video:height": 360,
        }
    }

    assert expected_info == page_info


def test_get_page_info_valid_id_live(monkeypatch, live_video_info):
    def mock_extract_info(*args, **kwargs):
        return live_video_info

    monkeypatch.setattr(YoutubeDL, "extract_info", mock_extract_info)

    video_id = "NlBLeMiRKT4"
    page_info = get_page_info(video_id)

    expected_info = {
        "title": "Live High-Definition Views from the International Space Station (Official NASA Stream) 2024-08-27 01:56",
        "description": "Live views from the International Space Station are streaming from an external camera mounted on the station's Harmony module. \n\nThe camera is looking forward at an angle so that International Docking Adapter 2 is visible. If the Harmony module camera is not available due to operational considerations for a longer period of time, a continuous loop of recorded Earth views will be displayed with the caption \u201cPreviously Recorded.\u201d\n\nThe space station orbits Earth about 250 miles (425 kilometers) above the surface. An international partnership of five space agencies from 15 countries operates the station, and it has been continuously occupied since November 2000. It's a microgravity laboratory where science, research, and human innovation make way for new technologies and research breakthroughs not possible on Earth. More: https://go.nasa.gov/3CkVtC8\n\nDid you know you can spot the station without a telescope? It looks like a fast-moving star, but you have to know when to look up. Sign up for text messages or email alerts to let you know when (and where) to spot the station and wave to the crew: https://spotthestation.nasa.gov\n\nhttps://nasa.gov/iss\n\nCredit: NASA",
        "original_url": "https://www.youtube.com/watch?v=NlBLeMiRKT4",
        "og_info": {
            "og:title": "Live High-Definition Views from the International Space Station (Official NASA Stream) 2024-08-27 01:56",
            "og:description": "Live views from the International Space Station are streaming from an external camera mounted on the station's Harmony module. \n\nThe camera is looking forward at an angle so that International Docking Adapter 2 is visible. If the Harmony module camera is not available due to operational considerations for a longer period of time, a continuous loop of recorded Earth views will be displayed with the caption \u201cPreviously Recorded.\u201d\n\nThe space station orbits Earth about 250 miles (425 kilometers) above the surface. An international partnership of five space agencies from 15 countries operates the station, and it has been continuously occupied since November 2000. It's a microgravity laboratory where science, research, and human innovation make way for new technologies and research breakthroughs not possible on Earth. More: https://go.nasa.gov/3CkVtC8\n\nDid you know you can spot the station without a telescope? It looks like a fast-moving star, but you have to know when to look up. Sign up for text messages or email alerts to let you know when (and where) to spot the station and wave to the crew: https://spotthestation.nasa.gov\n\nhttps://nasa.gov/iss\n\nCredit: NASA",
            "og:type": "website",
            "og:image": "https://i.ytimg.com/vi/NlBLeMiRKT4/maxresdefault.jpg",
            "og:url": "https://www.youtube.com/watch?v=NlBLeMiRKT4",
            "og:site_name": "FixTube",
        }
    }

    assert expected_info == page_info


def test_get_page_info_invalid_id(app, monkeypatch):
    def mock_extract_info(*args, **kwargs):
        raise YoutubeDLError("video not found")

    monkeypatch.setattr(YoutubeDL, "extract_info", mock_extract_info)

    video_id = "dQw4w9WgXcQ"

    with app.app_context():
        page_info = get_page_info(video_id)
        assert page_info == {}
