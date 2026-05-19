from __future__ import annotations

from taskq.backends.base import Backend


def reap_stalled(backend: Backend, grace_seconds: int = 60) -> int:
    """
    Requeue running jobs whose heartbeat has not been updated within
    `grace_seconds`. Returns the number of jobs requeued.
    """
    raise NotImplementedError
