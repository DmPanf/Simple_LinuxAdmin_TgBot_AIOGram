#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 28-05-2021

#import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from myconfig import *

#MyMsg = "*%s*, Привет! \xF0\x9F\x91\x80 Выбираем задачу:"               # Стартовое приглашение после ввода Кодового Слова
#foto1 = 'AgADAgADfqkxG2r6mEuUhFtqBaBgwdrdtw4ABKnYUDKtE82vcSkCAAEC' # tiger
em00 = "♻️"

uid01 = USER_ID_01          # My Main ID
#uid11 = USER_ID_11          # VVM Main ID
TOKEN = TOKEN_11            # [⚙️ VTI Comp Assistant💡] = vti-monitor {New Bot [27-05-2021] for vvm}
bot = Bot(token=TOKEN)      # Объект бота
dp = Dispatcher(bot)        # Диспетчер для бота
# Configure logging
logging.basicConfig(level=logging.INFO) # Включаем логирование, чтобы не пропустить важные сообщения
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# [START] Хэндлер на команду [/1307] = кодовое слово для доступа к Боту
@dp.message_handler(commands="1307")
async def process_start_command(message: types.Message): # присваиваем любое название функции
    cid = message.chat.id
#    await message.reply(str(cid))
    if str(cid) in str(ID):
       keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)
       # default row_width is 3, so here we can omit it actually
       btns_text = ('Yes!', 'No!')
       keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
       # adds buttons as a new row to the existing keyboard
       # the behaviour doesn't depend on row_width attribute

       more_btns_text = (
          "I don't know",
          "Who am i?",
          "Where am i?",
          "Who is there?",
       )
       keyboard_markup.add(*(types.KeyboardButton(text) for text in more_btns_text))
       # adds buttons. New rows are formed according to row_width parameter
       with open('../data/01.jpg', 'rb') as photo:
          await message.reply_photo(photo, caption="Hi!\nDo you like aiogram? 😷", reply_markup=keyboard_markup)
    else:
       await handle_all_messages(message)

@dp.message_handler()
async def all_msg_handler(message: types.Message):
    # pressing of a KeyboardButton is the same as sending the regular message with the same text
    # so, to handle the responses from the keyboard, we need to use a message_handler
    # in real bot, it's better to define message_handler(text="...") for each button
    # but here for the simplicity only one handler is defined

    button_text = message.text
    logger.debug('The answer is %r', button_text)  # print the text we've got

    if button_text == 'Yes!':
        reply_text = "That's great"
    elif button_text == 'No!':
        reply_text = "Oh no! Why?"
    else:
        reply_text = "**Keep calm...Everything is fine**"

    await message.reply(reply_text, reply_markup=types.ReplyKeyboardRemove())
    # with message, we send types.ReplyKeyboardRemove() to hide the keyboard

@dp.message_handler(content_types=['text'])
async def handle_all_messages(message):
    cid = message.chat.id
#    today = datetime.now(tz)           #====== логгирование заходов в Бот на Второй телефон
#    now = today.strftime("%H:%M")
#    if str(cid) in str(ID):
#       Name = MyID[str(cid)]
#    else:
#       Name = "None"
    Now = "28-05-2021"
    Name = str(cid)
    my_log = "Test-Bot: " + str(cid) + "=**" + Name + " ->** " + Now
    await bot.send_message(ID[1], my_log)  #====== END Logging
    await bot.send_message(cid, 'Hello World! %s' % em00)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)   # Запуск бота
