"""Landing page blueprint module."""
from __future__ import annotations

from datetime import datetime, timezone
import logging
from typing import Any, Dict

from app.lib.flask_compat import Blueprint, render_template

try:  # pragma: no cover - optional import in offline tests
    from flask import request
except ModuleNotFoundError:  # pragma: no cover - fallback for stubbed Flask
    request = None  # type: ignore[assignment]

landing_bp = Blueprint("landing", __name__, url_prefix="/landing/przechowanie-sprzetu-rekreacyjnego")
logger = logging.getLogger("app.landing.events")


@landing_bp.get("/landing")
def landing_home() -> str:
    """Render the base landing page template."""
    current_year = datetime.now(timezone.utc).year
    return render_template("landing/base.html", current_year=current_year)


@landing_bp.route("/landing/events", methods=("POST",))
def landing_event_ping() -> tuple[str, int]:
    """Receive async telemetry events from the landing page CTA interactions."""

    payload: Dict[str, Any] = {}
    user_agent = ""

    if request is not None:
        payload = request.get_json(silent=True) or {}
        user_agent = request.headers.get("User-Agent", "")

    event_name = str(payload.get("event", "")).strip()
    detail = payload.get("detail")

    if event_name:
        logger.info("Landing event captured", extra={"event": event_name, "detail": detail, "user_agent": user_agent})
    else:
        logger.info("Landing telemetry ping without event name", extra={"payload": payload, "user_agent": user_agent})

    return "", 204
