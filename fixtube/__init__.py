import os
from flask import Flask, request, abort, render_template, url_for
from flask_caching import Cache
import sentry_sdk
from .utils import get_page_info

if (sentry_dsn := os.getenv("SENTRY_DSN")) is not None:
    sentry_sdk.init(dsn=sentry_dsn)


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    cache = Cache(app)

    app_info = {
        "app_version": app.config["APP_VERSION"],
        "home_page": app.config["HOME_PAGE"],
        "issue_page": app.config["ISSUE_PAGE"],
    }

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
            "og:image": url_for("static", filename="fixtube.png")
        }

        return render_template("embed.html", **app_info, **page_info, og_info=og_info)

    # @app.route("/<video_id>")
    @app.route("/live/<video_id>")
    @app.route("/shorts/<video_id>")
    @app.route("/watch")
    def video(video_id: str | None = None):
        video_id = video_id or request.args.get("v")

        if video_id is None or video_id.strip() == "":
            abort(404)

        page_info = cache.get(video_id)

        if page_info is None:
            page_info = get_page_info(video_id)
            cache.set(video_id, page_info)

        if page_info == {}:
            abort(404)

        return render_template("embed.html", **app_info, **page_info)

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
            "og:image": url_for("static", filename="fixtube.png")
        }

        return render_template("embed.html", **app_info, **page_info, og_info=og_info), 404

    @app.errorhandler(500)
    def server_error(error):
        page_info = {
            "title": "Internal Server Error",
            "description": "There is something wrong.",
        }

        og_info = {
            "og:title": "Internal Server Error",
            "og:description": "There is something wrong.",
            "og:site_name": "FixTube",
            "og:type": "website",
            "og:image": url_for("static", filename="fixtube.png")
        }

        return render_template("embed.html", **app_info, **page_info, og_info=og_info), 500

    return app
