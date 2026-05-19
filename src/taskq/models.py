from __future__ import annotations

import enum
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


class JobStatus(str, enum.Enum):
    PENDING   = "pending"
    RUNNING   = "running"
    DONE      = "done"
    FAILED    = "failed"
    DEAD      = "dead"
    CANCELLED = "cancelled"


@dataclass
class JobRecord:
    # Identity
    id: str
    task_name: str
    queue: str = "default"

    # Lifecycle
    status: JobStatus = JobStatus.PENDING
    attempt: int = 0
    max_attempts: int = 1

    # Payload & Result
    payload: dict[str, Any] = field(default_factory=dict)
    result: dict[str, Any] | None = None
    error: str | None = None
    events: list[dict[str, Any]] = field(default_factory=list)

    # Routing
    worker_id: str | None = None
    parent_job_id: str | None = None

    # Timing
    created_at: datetime = field(default_factory=datetime.utcnow)
    scheduled_at: datetime = field(default_factory=datetime.utcnow)
    started_at: datetime | None = None
    completed_at: datetime | None = None
    last_heartbeat_at: datetime | None = None
    duration_ms: int | None = None

    @classmethod
    def from_row(cls, row: Any) -> "JobRecord":
        raise NotImplementedError


class JobHandle:
    """Lightweight reference to an enqueued job returned by .enqueue()."""

    def __init__(self, job_id: str, backend: Any) -> None:
        self.id = job_id
        self._backend = backend
        self._record: JobRecord | None = None

    @property
    def status(self) -> JobStatus:
        raise NotImplementedError

    @property
    def result(self) -> Any:
        raise NotImplementedError

    @property
    def error(self) -> str | None:
        raise NotImplementedError

    def wait(self, timeout: float = 30.0) -> "JobHandle":
        """Block until the job reaches a terminal state or timeout expires."""
        raise NotImplementedError

    def cancel(self) -> bool:
        raise NotImplementedError

    def refresh(self) -> "JobHandle":
        raise NotImplementedError
