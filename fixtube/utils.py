from yt_dlp import YoutubeDL
from yt_dlp.utils import YoutubeDLError


def get_ytdl_info(video_id: str):
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    options = {
        "dump_single_json": True,
    }

    ytdl = YoutubeDL(options)

    try:
        info = ytdl.extract_info(video_url, download=False)
        return info
    except YoutubeDLError:
        return None
