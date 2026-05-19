"""
Minimal getting-started example.

Usage:
    pip install taskq
    python examples/basic/app.py        # enqueue a job
    taskq worker --app examples.basic.app
    taskq dashboard                     # http://localhost:8765
"""

from taskq import task, TaskQ

taskq = TaskQ("sqlite:///jobs.db")


@task(queue="default", retries=3)
def crunch(n: int) -> int:
    return n * 2


if __name__ == "__main__":
    job = crunch.enqueue(n=21)
    print(f"Enqueued: {job.id}")
    print("Run: taskq worker --app examples.basic.app")
    print("Then: taskq dashboard")
