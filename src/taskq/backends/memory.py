from __future__ import annotations

from typing import Any

from taskq.backends.base import Backend
from taskq.models import JobRecord, JobStatus


class MemoryBackend(Backend):
    """
    In-process synchronous backend for unit testing.
    Jobs are executed inline on enqueue — no worker process needed.
    """

    def __init__(self) -> None:
        self._jobs: dict[str, JobRecord] = {}

    def enqueue(self, job: JobRecord) -> JobRecord:
        raise NotImplementedError

    def claim_next(self, queues: list[str], worker_id: str) -> JobRecord | None:
        raise NotImplementedError

    def heartbeat(self, job_id: str) -> None:
        raise NotImplementedError

    def complete(self, job_id: str, result: dict[str, Any]) -> None:
        raise NotImplementedError

    def fail(self, job_id: str, error: str, requeue: bool, delay_s: int) -> None:
        raise NotImplementedError

    def append_event(self, job_id: str, event: dict[str, Any]) -> None:
        raise NotImplementedError

    def get(self, job_id: str) -> JobRecord | None:
        raise NotImplementedError

    def list(
        self,
        queue: str | None = None,
        status: JobStatus | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> list[JobRecord]:
        raise NotImplementedError

    def cancel(self, job_id: str) -> bool:
        raise NotImplementedError

    def requeue(self, job_id: str) -> JobRecord:
        raise NotImplementedError

    def reap_stalled(self, grace_seconds: int) -> int:
        raise NotImplementedError

    def stats(self) -> dict[str, Any]:
        raise NotImplementedError
