import pytest

from taskq import task


def test_task_decorator_sets_queue():
    @task(queue="email", retries=3)
    def my_task(x: int) -> int:
        return x * 2

    assert my_task.queue == "email"
    assert my_task.retries == 3


def test_task_is_directly_callable():
    @task(queue="default")
    def add(a: int, b: int) -> int:
        return a + b

    assert add(1, 2) == 3


def test_task_name_is_dotted_path():
    @task()
    def my_fn() -> None:
        pass

    assert "my_fn" in my_fn.task_name


def test_enqueue_returns_job_handle():
    pytest.skip("Not implemented yet")
