"""Minimal JSON logging helpers used by the application."""

from __future__ import annotations

import json
import logging
from typing import Iterable


class JsonFormatter(logging.Formatter):
    """Simple JSON formatter compatible with the python-json-logger interface."""

    def __init__(self, fmt: str | None = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._fields = tuple(self._extract_fields(fmt))

    def format(self, record: logging.LogRecord) -> str:
        record.message = record.getMessage()
        record.asctime = self.formatTime(record, self.datefmt)

        payload = {}
        for field in self._fields:
            value = getattr(record, field, None)
            if value is not None:
                payload[field] = value

        if "message" not in payload:
            payload["message"] = record.message

        if "asctime" not in payload:
            payload["asctime"] = record.asctime

        return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))

    @staticmethod
    def _extract_fields(fmt: str | None) -> Iterable[str]:
        if not fmt:
            return ("asctime", "message")

        fields: list[str] = []
        for token in fmt.split():
            if token.startswith("%(") and token.endswith(")s"):
                fields.append(token[2:-2])
        return fields or ("asctime", "message")

