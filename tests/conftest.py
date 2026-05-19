import pytest

from taskq import TaskQ


@pytest.fixture
def memory_taskq() -> TaskQ:
    return TaskQ("memory://")


@pytest.fixture
def memory_backend(memory_taskq: TaskQ):
    return memory_taskq.backend
