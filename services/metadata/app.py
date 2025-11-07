"""FastAPI application stub for the metadata service."""

from __future__ import annotations

import importlib
from typing import Any


def create_app():
    """Construct the FastAPI application."""

    try:
        module = importlib.import_module("fastapi")
    except ModuleNotFoundError as exc:  # pragma: no cover - library required at runtime
        msg = "fastapi must be installed to initialize the metadata service."
        raise RuntimeError(msg) from exc

    fastapi_cls: Any = getattr(module, "FastAPI")
    app = fastapi_cls(title="Metadata Service", version="0.1.0")

    @app.get("/healthz")
    def health_check() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
