# Используем официальный образ Python 3.8
FROM python:3.8-slim-buster

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем код в контейнер
COPY . .

# Устанавливаем Poetry и зависимости
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Запускаем приложение
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

