from yt_dlp import YoutubeDL
from yt_dlp.utils import YoutubeDLError


def get_video_url(formats: list[dict]) -> str | None:
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
    best_format = max(video_formats, key=lambda f: int(f["height"]) * int(f["width"]))

    url = best_format["url"]
    return url


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
