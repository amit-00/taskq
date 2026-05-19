from __future__ import annotations

import threading

from taskq.backends.base import Backend


class HeartbeatThread(threading.Thread):
    """Daemon thread that pings the backend at a fixed interval while a job runs."""

    def __init__(self, job_id: str, backend: Backend, interval: int = 30) -> None:
        super().__init__(daemon=True, name=f"heartbeat-{job_id}")
        self.job_id = job_id
        self.backend = backend
        self.interval = interval
        self._stop_event = threading.Event()

    def run(self) -> None:
        raise NotImplementedError

    def stop(self) -> None:
        self._stop_event.set()
        self.join(timeout=self.interval + 1)
