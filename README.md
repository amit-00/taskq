# taskq

A durable, observable task queue for Python with first-class support for AI/agentic workloads.

## Install

```bash
pip install taskq                # SQLite backend, zero infra
pip install taskq[redis]         # + Redis backend
pip install taskq[dashboard]     # + web dashboard
pip install taskq[all]           # everything
```

## Quick Start

```python
from taskq import task, TaskQ

taskq = TaskQ("sqlite:///jobs.db")

@task(queue="default", retries=3)
def crunch(n: int) -> int:
    return n * 2

job = crunch.enqueue(n=21)
print(job.id)
```

```bash
taskq worker --app myapp     # process jobs
taskq dashboard              # open http://localhost:8765
```

## CLI

```bash
taskq worker --app myapp --queues email,default --concurrency 4
taskq dashboard
taskq status
taskq retry <job-id>
taskq cancel <job-id>
taskq purge --queue default --status done --older-than 7d
taskq inspect <job-id>
```

## Backends

| URL | Behaviour |
|---|---|
| `sqlite:///jobs.db` | Default. File-based, zero infra. |
| `sqlite:///:memory:` | In-memory SQLite — for integration tests. |
| `memory://` | Synchronous in-process execution. For unit tests. |
| `redis://localhost:6379` | Production Redis backend. |

## Status

Under active development. See the [design spec](./SPEC.md) for the full roadmap.
