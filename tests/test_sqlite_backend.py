import pytest

from taskq.backends.sqlite import SQLiteBackend


@pytest.fixture
def backend(tmp_path) -> SQLiteBackend:
    return SQLiteBackend(str(tmp_path / "test.db"))


def test_enqueue_and_get(backend: SQLiteBackend):
    pytest.skip("Not implemented yet")


def test_claim_next_atomicity(backend: SQLiteBackend):
    pytest.skip("Not implemented yet")


def test_complete_job(backend: SQLiteBackend):
    pytest.skip("Not implemented yet")


def test_fail_and_requeue(backend: SQLiteBackend):
    pytest.skip("Not implemented yet")


def test_dead_after_max_attempts(backend: SQLiteBackend):
    pytest.skip("Not implemented yet")


def test_cancel_pending_job(backend: SQLiteBackend):
    pytest.skip("Not implemented yet")


def test_reap_stalled(backend: SQLiteBackend):
    pytest.skip("Not implemented yet")


def test_stats_returns_counts(backend: SQLiteBackend):
    pytest.skip("Not implemented yet")
