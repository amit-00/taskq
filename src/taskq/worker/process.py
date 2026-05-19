from __future__ import annotations

import multiprocessing
from typing import Any

from taskq.backends.base import Backend


class Worker:
    """
    Supervisor process. Manages a pool of job subprocesses, runs the watchdog,
    and enforces per-queue rate limits.
    """

    def __init__(
        self,
        backend: Backend,
        queues: list[str],
        concurrency: int,
        poll_interval: float = 1.0,
        worker_id: str | None = None,
        rate_limits: dict[str, Any] | None = None,
    ) -> None:
        self.backend = backend
        self.queues = queues
        self.concurrency = concurrency
        self.poll_interval = poll_interval
        self.worker_id = worker_id or _default_worker_id()
        self.rate_limits = rate_limits or {}
        self._active: dict[str, multiprocessing.Process] = {}
        self._running = False

    def start(self) -> None:
        """Enter the supervisor loop. Blocks until stop() is called."""
        raise NotImplementedError

    def stop(self) -> None:
        raise NotImplementedError

    def _tick(self) -> None:
        """Single iteration: fill free slots, collect finished procs, run watchdog."""
        raise NotImplementedError

    def _handle_exit(self, job_id: str, exitcode: int) -> None:
        raise NotImplementedError


def _default_worker_id() -> str:
    import os
    import socket
    return f"{socket.gethostname()}-{os.getpid()}"
