"""Application factory for the Schowane landing page project."""
from __future__ import annotations

from pathlib import Path

from app.lib.flask_compat import Flask


def create_app() -> Flask:
    """Create and configure the Flask application instance."""
    project_root = Path(__file__).resolve().parent.parent
    app = Flask(
        __name__,
        static_folder=str(project_root / "static"),
        template_folder=str(project_root / "templates"),
    )

    from .landing import landing_bp  # noqa: WPS433 (delayed import to register blueprint)

    app.register_blueprint(landing_bp)

    @app.get("/")
    def index() -> tuple[str, int]:
        """Return a simple index response.

        The root route redirects users to the landing page implementation once it is ready.
        For now we return a placeholder response to confirm the app is running.
        """

        return "Schowane landing page backend is running.", 200

    return app
