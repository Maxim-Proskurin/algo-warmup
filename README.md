**algo-warmup** — коллекция крошечных задач для прокачки базового Python:
типизация, TDD, линтеры и CI.

[![CI](https://github.com/Maxim-Proskurin/algo-warmup/actions/workflows/ci.yml/badge.svg)](…)
![Python](https://img.shields.io/badge/python-3.12+-blue)
![coverage](https://img.shields.io/badge/coverage-97%25-brightgreen)

## 🚀 Быстрый старт

```bash
# клон и окружение
git clone https://github.com/Maxim-Proskurin/algo-warmup.git
cd algo-warmup
python -m venv .venv && source .venv/bin/activate   # Win: .venv\Scripts\activate
pip install -r requirements.txt

# линтеры и тесты
ruff check .
mypy .
pytest -q
```

---

## ✔️ Реализованные задачи

| Файл                 | Задача                             | Сложность    |
| -------------------- | ---------------------------------- | ------------ |
| `src/max_two_sum.py` | сумма двух max‑элементов           | `O(n)`       |
| `src/kth_largest.py` | k‑я по величине (MinHeap)          | `O(n log k)` |
| `src/utils.py`       | `get_env`, `time_ms` (monkeypatch) | —            |

---

## 🛠️ Стек

- Python 3.12\* ruff + mypy `--strict`\* pytest + coverage

---

## 📚 Полезные команды

| Команда                                                                                                     | Что делает             |
| ----------------------------------------------------------------------------------------------------------- | ---------------------- |
| `ruff check . --fix`                                                                                        | авто‑правка стиля      |
| `pytest --cov=src`                                                                                          | тесты + отчёт покрытия |
| `python -m timeit -n 100 -s "from src.kth_largest import kth_largest" "kth_largest(list(range(1000)), 10)"` | быстрая бенч‑проверка  |

---

## 🌱 Roadmap

-

---

## ⚖️ Лицензия

MIT © 2025 Maxim Proskurin
