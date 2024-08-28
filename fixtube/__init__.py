from flask import Flask, request, abort, render_template
from .utils import get_page_info


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Hello!"

    @app.route("/<video_id>")
    @app.route("/live/<video_id>")
    @app.route("/shorts/<video_id>")
    @app.route("/watch")
    def show_embed(video_id: str | None = None):
        video_id = video_id or request.args.get("v")

        if video_id is None or video_id.strip() == "":
            abort(404)

        page_info = get_page_info(video_id)

        if page_info is None:
            abort(404)

        return render_template("embed.html", **page_info)

    return app
