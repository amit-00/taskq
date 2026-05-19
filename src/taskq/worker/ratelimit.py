from __future__ import annotations

import threading
import time


class TokenBucket:
    """Thread-safe token bucket for per-queue rate limiting."""

    def __init__(self, rate: float, capacity: float) -> None:
        self._rate = rate        # tokens per second
        self._capacity = capacity
        self._tokens = capacity
        self._last_refill = time.monotonic()
        self._lock = threading.Lock()

    def consume(self, tokens: float = 1.0) -> bool:
        """Attempt to consume `tokens`. Returns True if allowed, False if rate-limited."""
        raise NotImplementedError

    @classmethod
    def from_string(cls, rate_str: str) -> "TokenBucket":
        """
        Parse a rate string and return a TokenBucket.
        Supported formats: '10/min', '100/hour', '5/sec'.
        """
        raise NotImplementedError
