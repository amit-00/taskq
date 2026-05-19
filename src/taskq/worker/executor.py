from __future__ import annotations

from collections.abc import Callable
from typing import Any

from taskq.backends.base import Backend
from taskq.models import JobRecord


def run_job(job: JobRecord, backend: Backend) -> None:
    """Entry point for the job subprocess. Resolves, executes, and finalises the job."""
    raise NotImplementedError


def resolve_task(task_name: str) -> Callable[..., Any]:
    """Import and return the callable identified by `task_name` (dotted module path)."""
    raise NotImplementedError


def accepts_ctx(fn: Callable[..., Any]) -> bool:
    """Return True if `fn` declares a `ctx` parameter."""
    raise NotImplementedError


def exponential_backoff(attempt: int, base: float = 5.0, max_delay: float = 3600.0) -> float:
    """Compute retry delay with jitter: min(base * 2^(attempt-1) + jitter, max_delay)."""
    raise NotImplementedError
