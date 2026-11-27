"""Presentation layer: web dashboard and JSON API."""
from flask import Blueprint, current_app, jsonify, render_template

from src.core.strength import estimate_frames, meets_contract, status

bp = Blueprint("ui", __name__, template_folder="templates")


def hive_summaries():
    repo = current_app.config["REPO"]
    out = []
    for r in repo.latest_per_hive():
        frames = estimate_frames(r["weight_kg"], r["temp_c"], r["sound_db"])
        out.append({
            "hive_id": r["hive_id"], "beekeeper": r["beekeeper"],
            "taken_at": r["taken_at"], "frames": frames,
            "meets_contract": meets_contract(frames), "status": status(frames),
        })
    return out


@bp.route("/")
def dashboard():
    hives = hive_summaries()
    passing = sum(h["meets_contract"] for h in hives)
    return render_template("dashboard.html", hives=hives, passing=passing)


@bp.route("/api/hives")
def api_hives():
    return jsonify(hive_summaries())


@bp.route("/health")
def health():
    return jsonify(status="ok")
