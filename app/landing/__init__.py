"""Landing page blueprint module."""
from __future__ import annotations

from datetime import datetime, timezone

from app.lib.flask_compat import Blueprint, render_template

landing_bp = Blueprint("landing", __name__)


@landing_bp.get("/landing")
def landing_home() -> str:
    """Render the base landing page template."""
    current_year = datetime.now(timezone.utc).year
    return render_template("landing/base.html", current_year=current_year)
