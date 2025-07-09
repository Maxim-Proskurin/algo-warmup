
from src.utils import get_env, time_ms

def test_get_env(monkeypatch):
    monkeypatch.setenv("API_KEY", "42")
    assert get_env("API_KEY", "X") == "42"
    assert get_env("MISSING", "fallback") == "fallback"

def test_time_ms(monkeypatch):
    monkeypatch.setattr("time.time", lambda: 123.456)
    assert time_ms() == 123456
