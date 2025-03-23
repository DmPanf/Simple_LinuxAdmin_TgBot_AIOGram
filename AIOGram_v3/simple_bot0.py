#@title 🔘 Описание бота

import asyncio
import os
import json
import nest_asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.client.bot import DefaultBotProperties
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Применяем nest_asyncio для корректной работы event loop в Google Colab
nest_asyncio.apply()

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = (f"🚀 Бот запущен успешно в <b>{now}</b>!\n"
                f"Каталоги созданы: <b>{IMAGES_FOLDER}</b> и <b>{RESULTS_FOLDER}</b>.\n"
                f"📅 Можно использовать команду <code>/date</code>, чтобы вывести текущую дату и время!\n"
                f"... или <b>/help</b>, чтобы увидеть список доступных команд.")
    await message.reply(response)
    logger.info(f"Отправлено сообщение при старте: {response}")
    print(f"Отправлено сообщение при старте: {response}")

# Обработчик команды /date - выводит текущую дату и время
@dp.message(Command("date"))
async def cmd_date(message: types.Message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = f"Текущая дата и время: <b>{now}</b>."
    await message.reply(response)
    logger.info(f"Отправлено сообщение с датой: {response}")
    print(f"Отправлено сообщение с датой: {response}")

# Обработчик команды /help - выводит текущую дату и время
@dp.message(Command("help"))
async def cmd_date(message: types.Message):
    response = f"📚 Доступные команды:\n" \
               f"<code>/start</code> - Запуск бота\n" \
               f"<code>/date</code> - Вывод текущей даты и времени\n" \
               f"<code>/help</code> - Вывод доступных команд"
    await message.reply(response)
    logger.info(f"Отправлено сообщение с командами: {response}")
    print(f"Отправлено сообщение с командами: {response}")

# Универсальный обработчик для логирования входящих сообщений (игнорируем команды)
@dp.message()
async def log_all_messages(message: types.Message):
    if message.text and message.text.startswith('/'):
        # Если сообщение является командой, пропускаем логирование, чтобы команда отработала отдельно.
        return
    user_info = f"{message.from_user.id} - {message.from_user.full_name}" if message.from_user else "Unknown user"
    log_text = f"Получено сообщение от {user_info}: {message.text}"
    logger.info(log_text)
    print(log_text)

# Функция для запуска бота
async def main():
    logger.info("Запуск polling бота...")
    print("Запуск polling бота...")
    await dp.start_polling(bot)

# Запуск бота в Google Colab
if __name__ == '__main__':
    asyncio.run(main())
