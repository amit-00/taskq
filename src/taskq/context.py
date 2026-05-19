from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from taskq.backends.base import Backend
    from taskq.models import JobRecord


class TaskContext:
    """Injected into tasks that declare `ctx: TaskContext`. Provides progress streaming."""

    def __init__(self, job: "JobRecord", backend: "Backend") -> None:
        self._job = job
        self._backend = backend

    def update(
        self,
        message: str,
        progress: float | None = None,
        data: dict[str, Any] | None = None,
    ) -> None:
        """Append a progress event. Also resets the watchdog timer."""
        raise NotImplementedError
