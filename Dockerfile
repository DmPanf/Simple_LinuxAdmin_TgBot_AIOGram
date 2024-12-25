# Dockerfile
# Используем официальный образ Python
FROM python:3.11

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы в рабочую директорию
COPY . .

# Указываем команду запуска
CMD ["python", "bot.py"]
