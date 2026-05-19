from __future__ import annotations

from collections.abc import Callable
from typing import Any

from taskq.models import JobHandle


def task(
    *,
    queue: str = "default",
    retries: int = 0,
    timeout: int = 300,
    heartbeat: int = 30,
    backoff: Callable[[int], float] | None = None,
) -> Callable[[Callable[..., Any]], "Task"]:
    """Register a function as a taskq task."""

    def decorator(fn: Callable[..., Any]) -> "Task":
        return Task(
            fn,
            queue=queue,
            retries=retries,
            timeout=timeout,
            heartbeat=heartbeat,
            backoff=backoff,
        )

    return decorator


class Task:
    """Produced by @task. Adds .enqueue() while keeping the function directly callable."""

    def __init__(
        self,
        fn: Callable[..., Any],
        *,
        queue: str,
        retries: int,
        timeout: int,
        heartbeat: int,
        backoff: Callable[[int], float] | None,
    ) -> None:
        self.fn = fn
        self.queue = queue
        self.retries = retries
        self.timeout = timeout
        self.heartbeat = heartbeat
        self.backoff = backoff
        self.__name__ = fn.__name__
        self.__doc__ = fn.__doc__

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.fn(*args, **kwargs)

    def enqueue(self, **kwargs: Any) -> JobHandle:
        raise NotImplementedError

    @property
    def task_name(self) -> str:
        """Fully qualified dotted name used to resolve this task in worker subprocesses."""
        return f"{self.fn.__module__}.{self.fn.__qualname__}"
