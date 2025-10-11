"""Compatibility helpers for importing Flask or providing a lightweight fallback."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable

try:  # pragma: no cover - prefer real Flask when available
    from flask import Blueprint, Flask, render_template, url_for, redirect  # type: ignore
except ModuleNotFoundError:  # pragma: no cover
    from .flask_stub import Blueprint, Flask, render_template, url_for, redirect  # noqa: F401


__all__ = ["Blueprint", "Flask", "render_template", "url_for"]
