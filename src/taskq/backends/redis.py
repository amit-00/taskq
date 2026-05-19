from __future__ import annotations

from typing import Any

from taskq.backends.base import Backend
from taskq.models import JobRecord, JobStatus

# Redis key layout:
#   taskq:queue:{name}            sorted set   score = scheduled_at (unix ts)
#   taskq:job:{id}                hash         all job fields
#   taskq:running                 sorted set   score = claimed_at
#   taskq:stats:{queue}:{status}  string       counter


class RedisBackend(Backend):
    """
    Redis backend using sorted-set queues and a Lua claim script for atomicity.
    Requires: pip install taskq[redis]
    """

    def __init__(self, url: str) -> None:
        self._url = url
        self._client: Any = None

    def _get_client(self) -> Any:
        """Lazy-init redis.Redis, raising ImportError if redis-py is not installed."""
        raise NotImplementedError

    def enqueue(self, job: JobRecord) -> JobRecord:
        raise NotImplementedError

    def claim_next(self, queues: list[str], worker_id: str) -> JobRecord | None:
        """Claim via Lua script: ZPOPMIN queue + ZADD running, atomically."""
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
