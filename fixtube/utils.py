from yt_dlp import YoutubeDL
from yt_dlp.utils import YoutubeDLError


def get_page_info(video_id: str):
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"
    info = get_ytdl_info(youtube_url)

    if info is None:
        return None

    title = info["title"]
    desc = info["description"]

    page_info = {
        "title": title,
        "description": desc,
        "original_url": youtube_url,
    }

    is_live = info["live_status"] == "is_live"

    video_format = None if is_live else get_best_format(info["formats"])

    opengraph_info = {
        "og:title": title,
        "og:description": desc,
        "og:type": "website",
        "og:image": info["thumbnail"],
        "og:url": youtube_url,
        "og:site_name": "FixTube",
    }

    if video_format is not None:
        og_video_info = {
            "og:type": "video.movie",
            "og:video": video_format["url"],
            "og:video:secure_url": video_format["url"],
            "og:video:type": f"video/{video_format['ext']}",
            "og:video:width": video_format["width"],
            "og:video:height": video_format["height"],
        }

        opengraph_info.update(og_video_info)

    page_info["og_info"] = opengraph_info

    return page_info


def get_best_format(formats: list[dict]):
    def is_good_format(format: dict):
        # check if format has video codec
        if "vcodec" not in format or format["vcodec"] == "none":
            return False

        # check if format has audio codec
        if "acodec" not in format or format["acodec"] == "none":
            return False

        return True

    # filter non video format
    video_formats = list(filter(is_good_format, formats))

    if len(video_formats) == 0:
        return None

    # get best video format with highest resolution
    best_format = max(video_formats, key=lambda f: f["height"] * f["width"])
    return best_format


def get_ytdl_info(url: str):
    options = {
        "dump_single_json": True,
    }

    ytdl = YoutubeDL(options)

    try:
        info = ytdl.extract_info(url, download=False)
        return info
    except YoutubeDLError:
        return None
