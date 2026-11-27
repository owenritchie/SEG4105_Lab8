"""HiveCheck entry point."""
import os

from flask import Flask

from src.data.repository import ReadingRepository
from src.ui.routes import bp


def create_app():
    app = Flask(__name__)
    repo = ReadingRepository(os.environ.get("HIVECHECK_DB", ":memory:"))
    repo.seed_demo_data()
    app.config["REPO"] = repo
    app.register_blueprint(bp)
    return app


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    create_app().run(host="0.0.0.0", port=port)
