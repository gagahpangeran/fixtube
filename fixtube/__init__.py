from flask import Flask, request, abort


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

        return video_id

    return app
