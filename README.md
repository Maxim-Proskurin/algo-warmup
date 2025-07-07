# 🧩 algo-warmup

Набор маленьких алгоритмических задач для прокачки Python-базы  
(типизация, TDD, линтеры, CI).

## 📦 Установка

```bash
git clone https://github.com/Maxim-Proskurin/algo-warmup.git
cd algo-warmup
python -m venv .venv && source .venv/bin/activate    # Win: .venv\Scripts\activate
pip install -r requirements.txt

```🚀 Быстрый старт
ruff check .
mypy .
pytest -q

✔️ Реализованные задачи
Файл	src/max_two_sum.py	сумма двух max-элементов

🏗️ CI

✨ Планы
 добавить kth_largest

 тренировка monkeypatch

 покрытие > 90 %