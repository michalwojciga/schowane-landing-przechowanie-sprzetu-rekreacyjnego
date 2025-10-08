"""Minimal Flask-like fallback used when the real Flask package is unavailable."""
from __future__ import annotations

from dataclasses import dataclass
from http import HTTPStatus
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, MutableMapping
import re

TemplateContext = Mapping[str, Any]
ViewReturn = Any


@dataclass
class _Route:
    methods: tuple[str, ...]
    rule: str
    view_func: Callable[..., ViewReturn]


class Flask:
    """Lightweight subset of the Flask API used for tests in offline environments."""

    def __init__(
        self,
        import_name: str,
        *,
        static_folder: str | None = "static",
        template_folder: str | None = "templates",
    ) -> None:
        self.import_name = import_name
        self.static_folder = static_folder
        self.template_folder = template_folder
        self.config: dict[str, Any] = {}
        self._routes: MutableMapping[tuple[str, str], Callable[..., ViewReturn]] = {}

    # routing API -----------------------------------------------------------
    def route(self, rule: str, methods: Iterable[str] | None = None) -> Callable[[Callable[..., ViewReturn]], Callable[..., ViewReturn]]:
        methods_tuple = tuple(method.upper() for method in (methods or ("GET",)))

        def decorator(func: Callable[..., ViewReturn]) -> Callable[..., ViewReturn]:
            for method in methods_tuple:
                self._routes[(method, rule)] = func
            return func

        return decorator

    def get(self, rule: str) -> Callable[[Callable[..., ViewReturn]], Callable[..., ViewReturn]]:
        return self.route(rule, methods=("GET",))

    def register_blueprint(self, blueprint: "Blueprint") -> None:
        for route in blueprint._routes:
            full_rule = f"{blueprint.url_prefix}{route.rule}" if blueprint.url_prefix else route.rule
            for method in route.methods:
                self._routes[(method, full_rule)] = route.view_func

    # testing ----------------------------------------------------------------
    def test_client(self) -> "_TestClient":
        return _TestClient(self)


class Blueprint:
    """Subset of Flask's Blueprint used for structuring routes."""

    def __init__(self, name: str, import_name: str, *, url_prefix: str | None = "") -> None:
        self.name = name
        self.import_name = import_name
        self.url_prefix = url_prefix or ""
        self._routes: list[_Route] = []

    def route(self, rule: str, methods: Iterable[str] | None = None) -> Callable[[Callable[..., ViewReturn]], Callable[..., ViewReturn]]:
        methods_tuple = tuple(method.upper() for method in (methods or ("GET",)))

        def decorator(func: Callable[..., ViewReturn]) -> Callable[..., ViewReturn]:
            self._routes.append(_Route(methods_tuple, rule, func))
            return func

        return decorator

    def get(self, rule: str) -> Callable[[Callable[..., ViewReturn]], Callable[..., ViewReturn]]:
        return self.route(rule, methods=("GET",))


class _TestResponse:
    def __init__(self, data: Any, status_code: int) -> None:
        if isinstance(data, bytes):
            self.data = data
        else:
            self.data = str(data).encode("utf-8")
        self.status_code = status_code


class _TestClient:
    def __init__(self, app: Flask) -> None:
        self._app = app

    def get(self, path: str) -> _TestResponse:
        view = self._app._routes.get(("GET", path))
        if view is None:
            return _TestResponse("", HTTPStatus.NOT_FOUND)

        result = view()
        data: Any
        status: int
        if isinstance(result, tuple):
            if len(result) == 3:
                data, status, _headers = result
            elif len(result) == 2:
                data, status = result
            else:
                data = result[0]
                status = HTTPStatus.OK
        else:
            data = result
            status = HTTPStatus.OK

        return _TestResponse(data, status)


def render_template(template_name: str, **_context: TemplateContext) -> str:
    template_path = _template_root() / template_name
    html = template_path.read_text(encoding="utf-8")
    return _resolve_static_urls(html)


def url_for(endpoint: str, **values: Any) -> str:
    if endpoint == "static":
        filename = values.get("filename")
        if not filename:
            raise ValueError("'filename' is required for static endpoint")
        return f"/static/{filename}"
    return f"/{endpoint}"


_STATIC_URL_RE = re.compile(r"\{\{\s*url_for\('static',\s*filename=['\"]([^'\"]+)['\"]\)\s*\}\}")


def _resolve_static_urls(html: str) -> str:
    return _STATIC_URL_RE.sub(lambda match: f"/static/{match.group(1)}", html)


def _template_root() -> Path:
    current = Path(__file__).resolve()
    templates_dir = current.parents[2] / "templates"
    if not templates_dir.exists():
        raise FileNotFoundError(f"Templates directory not found: {templates_dir}")
    return templates_dir
