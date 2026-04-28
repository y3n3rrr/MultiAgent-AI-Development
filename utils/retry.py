import time
from typing import Callable, TypeVar

T = TypeVar("T")


def retry(
    func: Callable[[], T],
    attempts: int = 3,
    delay_seconds: float = 0.5,
) -> T:
    last_error: Exception | None = None

    for attempt in range(1, attempts + 1):
        try:
            return func()
        except Exception as exc:
            last_error = exc
            if attempt < attempts:
                time.sleep(delay_seconds)

    raise RuntimeError(
        f"Operation failed after {attempts} attempts: {last_error}"
    ) from last_error
