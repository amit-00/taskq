from __future__ import annotations

from typing import Optional

import typer

app = typer.Typer(
    name="taskq",
    help="taskq — durable task queue CLI",
    no_args_is_help=True,
)


@app.command()
def worker(
    module: str = typer.Option(..., "--app", help="Module to import and scan for @task decorators"),
    queues: str = typer.Option("default", help="Comma-separated queue names to poll"),
    concurrency: int = typer.Option(0, help="Max parallel jobs (0 = CPU count)"),
    poll_interval: float = typer.Option(1.0, help="Seconds between polls when idle"),
    worker_id: Optional[str] = typer.Option(None, help="Unique worker name (default: hostname-pid)"),
    backend: Optional[str] = typer.Option(None, envvar="TASKQ_BACKEND", help="Backend URL override"),
) -> None:
    """Start a worker process."""
    raise NotImplementedError


@app.command()
def dashboard(
    host: str = typer.Option("127.0.0.1", envvar="TASKQ_DASHBOARD_HOST"),
    port: int = typer.Option(8765, envvar="TASKQ_DASHBOARD_PORT"),
    backend: Optional[str] = typer.Option(None, envvar="TASKQ_BACKEND"),
) -> None:
    """Start the web dashboard on the configured host and port."""
    raise NotImplementedError


@app.command()
def status(
    queue: Optional[str] = typer.Option(None, help="Filter to a single queue"),
    backend: Optional[str] = typer.Option(None, envvar="TASKQ_BACKEND"),
) -> None:
    """Print queue depths and job counts to stdout."""
    raise NotImplementedError


@app.command()
def retry(
    job_id: Optional[str] = typer.Argument(None, help="Specific job ID to retry"),
    queue: Optional[str] = typer.Option(None, help="Queue filter for bulk retry"),
    job_status: Optional[str] = typer.Option(None, "--status", help="Status filter for bulk retry"),
    task_name: Optional[str] = typer.Option(None, "--task", help="Task name filter for bulk retry"),
    backend: Optional[str] = typer.Option(None, envvar="TASKQ_BACKEND"),
) -> None:
    """Re-enqueue a failed or dead job (or bulk retry by queue/status)."""
    raise NotImplementedError


@app.command()
def cancel(
    job_id: str = typer.Argument(..., help="Job ID to cancel"),
    backend: Optional[str] = typer.Option(None, envvar="TASKQ_BACKEND"),
) -> None:
    """Cancel a pending job before it is picked up by a worker."""
    raise NotImplementedError


@app.command()
def purge(
    queue: str = typer.Option(..., help="Queue to purge"),
    job_status: str = typer.Option(..., "--status", help="Status of jobs to delete"),
    older_than: Optional[str] = typer.Option(None, "--older-than", help="Age threshold e.g. 7d, 24h"),
    backend: Optional[str] = typer.Option(None, envvar="TASKQ_BACKEND"),
) -> None:
    """Delete old job records matching the given queue, status, and age."""
    raise NotImplementedError


@app.command()
def inspect(
    job_id: str = typer.Argument(..., help="Job ID to inspect"),
    backend: Optional[str] = typer.Option(None, envvar="TASKQ_BACKEND"),
) -> None:
    """Print full job record as JSON."""
    raise NotImplementedError
