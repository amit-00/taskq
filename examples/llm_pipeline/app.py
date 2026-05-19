"""
LLM pipeline example — demonstrates TaskContext, job chaining, and rate limiting.

Usage:
    taskq worker --app examples.llm_pipeline.app --queues ai,default --concurrency 2
"""

from taskq import TaskContext, TaskQ, task

taskq = TaskQ(
    "sqlite:///jobs.db",
    queues={
        "ai": {"concurrency": 2, "rate_limit": "10/min"},
        "default": {"concurrency": 4},
    },
)


@task(queue="ai", timeout=300, heartbeat=30, retries=2)
def generate_summary(topic: str, ctx: TaskContext) -> str:
    ctx.update("Starting summary generation...", progress=0.0)
    # TODO: call your LLM here
    ctx.update("Done.", progress=1.0)
    return f"Summary of {topic}"


@task(queue="ai", timeout=600, heartbeat=30)
def process_document(doc_id: str, ctx: TaskContext) -> str:
    ctx.update(f"Processing document {doc_id}...", progress=0.0)

    summary_job = generate_summary.enqueue(topic=doc_id)
    ctx.update("Waiting for summary...", progress=0.5)

    result = summary_job.wait(timeout=120).result
    ctx.update("Pipeline complete.", progress=1.0)
    return result


if __name__ == "__main__":
    job = process_document.enqueue(doc_id="doc-001")
    print(f"Enqueued pipeline job: {job.id}")
