# /app/__init__.py

"""Application factory for the Schowane landing page project."""
from __future__ import annotations

from logging.config import dictConfig
from pathlib import Path

from app.lib.flask_compat import Flask, redirect, url_for

LOGGING = {
    "version": 1,
    "loggers": {
        "app.landing.events": {
            "handlers": ["cta_events", "newsletter"],
            "level": "INFO",
            "propagate": False,
        },
    },
    "handlers": {
        "cta_events": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "logs/landing-cta.log",
            "maxBytes": 5 * 1024 * 1024,
            "backupCount": 5,
            "formatter": "json",
        },
        "newsletter": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "logs/newsletter.log",
            "maxBytes": 1 * 1024 * 1024,
            "backupCount": 3,
            "encoding": "utf-8",
            "formatter": "json",
        },
    },
    "formatters": {
        "json": {
            "()": "app.lib.json_logging.JsonFormatter",
            "fmt": "%(asctime)s %(event)s %(detail)s %(user_agent)s",
        },
    },
}


def create_app() -> Flask:
    """Create and configure the Flask application instance."""
    project_root = Path(__file__).resolve().parent.parent
    logs_path = project_root / "logs"
    logs_path.mkdir(parents=True, exist_ok=True)

    LOGGING["handlers"]["cta_events"]["filename"] = str(
        logs_path / "landing-cta.log"
    )
    LOGGING["handlers"]["newsletter"]["filename"] = str(
        logs_path / "newsletter.log"
    )
    app = Flask(
        __name__,
        static_folder=str(project_root / "static"),
        template_folder=str(project_root / "templates"),
    )

    dictConfig(LOGGING)

    from .landing import landing_bp  # noqa: WPS433 (delayed import to register blueprint)

    app.register_blueprint(landing_bp)

    @app.get("/", strict_slashes=False)
    def index():
        """Return a simple index response.
        The root route redirects users to the landing page implementation once it is ready.
        For now we return a placeholder response to confirm the app is running.
        """
        return redirect(url_for("landing.landing_home"), code=301)

        #return "Schowane landing page backend is running.", 200

    return app
