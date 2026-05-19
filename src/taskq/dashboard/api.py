from __future__ import annotations

try:
    from fastapi import APIRouter
except ImportError as exc:
    raise ImportError("Install dashboard extras: pip install taskq[dashboard]") from exc

router = APIRouter(prefix="/api")


@router.get("/stats")
async def get_stats() -> dict:
    raise NotImplementedError


@router.get("/jobs")
async def list_jobs(
    queue: str | None = None,
    status: str | None = None,
    limit: int = 100,
    offset: int = 0,
) -> list[dict]:
    raise NotImplementedError


@router.get("/jobs/{job_id}")
async def get_job(job_id: str) -> dict:
    raise NotImplementedError


@router.post("/jobs/{job_id}/retry")
async def retry_job(job_id: str) -> dict:
    raise NotImplementedError


@router.post("/jobs/{job_id}/cancel")
async def cancel_job(job_id: str) -> dict:
    raise NotImplementedError


@router.post("/queues/{queue_name}/retry-all")
async def retry_all_dead(queue_name: str) -> dict:
    raise NotImplementedError


@router.get("/workers")
async def list_workers() -> list[dict]:
    raise NotImplementedError
