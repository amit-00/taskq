from __future__ import annotations

from typing import Any

from taskq.backends.base import Backend


class TaskQ:
    """Main entry point. Configures and holds a backend instance."""

    def __init__(
        self,
        backend_url: str,
        retention: dict[str, str | None] | None = None,
        queues: dict[str, dict[str, Any]] | None = None,
    ) -> None:
        self._url = backend_url
        self.retention: dict[str, str | None] = retention or {
            "done": "7d",
            "failed": "30d",
            "dead": None,
            "cancelled": "7d",
        }
        self.queues: dict[str, dict[str, Any]] = queues or {}
        self._backend: Backend | None = None

    @property
    def backend(self) -> Backend:
        raise NotImplementedError

    @staticmethod
    def _build_backend(url: str) -> Backend:
        """Parse a backend URL and return the appropriate Backend instance."""
        raise NotImplementedError
