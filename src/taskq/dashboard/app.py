from __future__ import annotations

try:
    from fastapi import FastAPI
except ImportError as exc:
    raise ImportError("Install dashboard extras: pip install taskq[dashboard]") from exc

from taskq.dashboard.api import router


def create_app(backend_url: str) -> FastAPI:
    """Build and return the configured FastAPI application."""
    raise NotImplementedError
