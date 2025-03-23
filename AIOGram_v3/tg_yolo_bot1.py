#@title Описание функций TgBot-2 для Google Colab
import asyncio
import os
import json
import nest_asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.client.bot import DefaultBotProperties
from aiogram.types import FSInputFile
import logging
from dotenv import load_dotenv

# Загрузка переменных из .env
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Применяем nest_asyncio для корректной работы event loop в Google Colab
nest_asyncio.apply()

# Конфигурация модели и диапазона классов
MODEL_PATH = "yolov8m-seg.pt"
DEFAULT_CLASSES = "[0:79]"

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

# Обработчик команды /help - выводит доступные команды
@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    response = ("📚 Доступные команды:\n"
                "<code>/start</code> - Запуск бота\n"
                "<code>/date</code> - Вывод текущей даты и времени\n"
                "<code>/help</code> - Вывод доступных команд\n"
                "<code>/setclasses [диапазон]</code> - Задать новый диапазон классов для сегментации (например, /setclasses [1:5])")
    await message.reply(response)
    logger.info(f"Отправлено сообщение с командами: {response}")
    print(f"Отправлено сообщение с командами: {response}")

# Обработчик команды /setclasses для установки нового диапазона классов
@dp.message(Command("setclasses"))
async def set_classes(message: types.Message):
    # Извлекаем аргументы вручную: ожидается формат "/setclasses аргументы"
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        response = "Пожалуйста, укажите диапазон классов, например: /setclasses [1:5] или /setclasses 1:5"
        await message.reply(response)
        return
    args = parts[1].strip()

    # Функция валидации диапазона классов
    def validate_class_range(arg: str) -> bool:
        arg_clean = arg.strip("[]")
        if ':' not in arg_clean:
            return False
        try:
            start_str, end_str = arg_clean.split(':', 1)
            start = int(start_str)
            end = int(end_str)
            return start <= end
        except ValueError:
            return False

    if not validate_class_range(args):
        response = ("❌ Неверный формат диапазона классов. "
                    "Пожалуйста, используйте формат [start:end], где start и end - целые числа, и start <= end.")
        await message.reply(response)
        return

    global DEFAULT_CLASSES
    DEFAULT_CLASSES = args
    response = f"✅ Новый диапазон классов установлен: {DEFAULT_CLASSES}\nЖду фотографий..."
    await message.reply(response)
    logger.info(response)
    print(response)

# Обработчик для фотографий с использованием фильтра F
@dp.message(F.content_type == "photo")
async def handle_photo(message: types.Message):
    # Выбираем фото с наилучшим разрешением
    photo = message.photo[-1]
    # Создаём папки, если их ещё нет
    os.makedirs(IMAGES_FOLDER, exist_ok=True)
    os.makedirs(RESULTS_FOLDER, exist_ok=True)
    input_path = os.path.join(IMAGES_FOLDER, "input.jpg")

    # Получаем информацию о файле и скачиваем его
    file_info = await bot.get_file(photo.file_id)
    await bot.download_file(file_info.file_path, destination=input_path)

    response_text = f"🔄 Обработка изображения с диапазоном классов: {DEFAULT_CLASSES}"
    await message.reply(response_text)
    logger.info(response_text)
    print(response_text)
    try:
        output_file = process_image(MODEL_PATH, image_name=input_path, classes=DEFAULT_CLASSES)
    except Exception as e:
        error_text = f"Ошибка при обработке изображения: {e}"
        await message.reply(error_text)
        logger.error(error_text)
        print(error_text)
        return
    # Перемещаем обработанный файл в папку результатов
    output_path = os.path.join(RESULTS_FOLDER, output_file)
    os.replace(output_file, output_path)

    # Отправляем обработанное изображение, используя FSInputFile
    from aiogram.types import FSInputFile
    photo_input = FSInputFile(output_path)
    await message.reply_photo(photo=photo_input, caption="✅ Обработанное изображение")
    logger.info("Отправлено обработанное изображение")
    print("Отправлено обработанное изображение")


# Универсальный обработчик для текстовых сообщений (чтобы не перехватывать фото)
@dp.message(F.content_type == "text")
async def log_all_text_messages(message: types.Message):
    if message.text and message.text.startswith('/'):
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
