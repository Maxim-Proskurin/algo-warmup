import os
import time

def get_env(key: str, default: str) -> str:
    """Вернуть значение переменной окружения или default, если переменной нет."""
    return os.getenv(key, default)

def time_ms() -> int:
    """Текущий Unix-timestamp в миллисекундах."""
    return int(time.time() * 1000)
