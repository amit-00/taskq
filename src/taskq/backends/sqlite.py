from __future__ import annotations

import sqlite3
from typing import Any

from taskq.backends.base import Backend
from taskq.models import JobRecord, JobStatus

DDL = """
CREATE TABLE IF NOT EXISTS jobs (
    id                TEXT PRIMARY KEY,
    task_name         TEXT NOT NULL,
    queue             TEXT NOT NULL DEFAULT 'default',
    status            TEXT NOT NULL DEFAULT 'pending',
    attempt           INTEGER NOT NULL DEFAULT 0,
    max_attempts      INTEGER NOT NULL DEFAULT 1,
    payload           TEXT NOT NULL DEFAULT '{}',
    result            TEXT,
    error             TEXT,
    events            TEXT NOT NULL DEFAULT '[]',
    worker_id         TEXT,
    parent_job_id     TEXT REFERENCES jobs(id),
    created_at        TEXT NOT NULL,
    scheduled_at      TEXT NOT NULL,
    started_at        TEXT,
    completed_at      TEXT,
    last_heartbeat_at TEXT,
    duration_ms       INTEGER
);

CREATE INDEX IF NOT EXISTS idx_jobs_queue_status ON jobs(queue, status, scheduled_at);
CREATE INDEX IF NOT EXISTS idx_jobs_parent       ON jobs(parent_job_id);
CREATE INDEX IF NOT EXISTS idx_jobs_task         ON jobs(task_name);
"""


class SQLiteBackend(Backend):
    """
    SQLite backend with WAL mode and atomic claim_next.
    Suitable for single-machine workloads up to ~100 jobs/sec.
    """

    def __init__(self, path: str) -> None:
        self._path = path
        self._conn: sqlite3.Connection | None = None

    def _connect(self) -> sqlite3.Connection:
        """Open (or return cached) connection with WAL mode enabled."""
        raise NotImplementedError

    def enqueue(self, job: JobRecord) -> JobRecord:
        raise NotImplementedError

    def claim_next(self, queues: list[str], worker_id: str) -> JobRecord | None:
        """Atomically claim next pending job via single UPDATE...RETURNING statement."""
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
