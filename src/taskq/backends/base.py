from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from taskq.models import JobRecord, JobStatus


class Backend(ABC):

    @abstractmethod
    def enqueue(self, job: JobRecord) -> JobRecord: ...

    @abstractmethod
    def claim_next(self, queues: list[str], worker_id: str) -> JobRecord | None: ...

    @abstractmethod
    def heartbeat(self, job_id: str) -> None: ...

    @abstractmethod
    def complete(self, job_id: str, result: dict[str, Any]) -> None: ...

    @abstractmethod
    def fail(self, job_id: str, error: str, requeue: bool, delay_s: int) -> None: ...

    @abstractmethod
    def append_event(self, job_id: str, event: dict[str, Any]) -> None: ...

    @abstractmethod
    def get(self, job_id: str) -> JobRecord | None: ...

    @abstractmethod
    def list(
        self,
        queue: str | None = None,
        status: JobStatus | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> list[JobRecord]: ...

    @abstractmethod
    def cancel(self, job_id: str) -> bool: ...

    @abstractmethod
    def requeue(self, job_id: str) -> JobRecord: ...

    @abstractmethod
    def reap_stalled(self, grace_seconds: int) -> int: ...

    @abstractmethod
    def stats(self) -> dict[str, Any]: ...
