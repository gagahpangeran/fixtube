from flask import Flask, request, abort, render_template
from .utils import get_page_info


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        page_info = {
            "title": "FixTube",
            "description": "Fix your youtube embed.",
            "original_url": "https://www.youtube.com",
        }

        og_info = {
            "og:title": "FixTube",
            "og:description": "Fix your youtube embed.",
            "og:site_name": "FixTube",
            "og:type": "website",
        }

        return render_template("embed.html", og_info=og_info, **page_info)

    @app.route("/<video_id>")
    @app.route("/live/<video_id>")
    @app.route("/shorts/<video_id>")
    @app.route("/watch")
    def video(video_id: str | None = None):
        video_id = video_id or request.args.get("v")

        if video_id is None or video_id.strip() == "":
            abort(404)

        page_info = get_page_info(video_id)

        if page_info is None:
            abort(404)

        return render_template("embed.html", **page_info)

    @app.errorhandler(404)
    def not_found(error):
        page_info = {
            "title": "Video not found",
            "description": "404 not found.",
            "original_url": "https://www.youtube.com",
        }

        og_info = {
            "og:title": "Video not found",
            "og:description": "404 not found.",
            "og:site_name": "FixTube",
            "og:type": "website",
        }

        return render_template("embed.html", og_info=og_info, **page_info), 404

    return app
