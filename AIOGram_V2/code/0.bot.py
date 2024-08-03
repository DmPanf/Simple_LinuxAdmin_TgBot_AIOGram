#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 28-05-2021
# -----| Пример выделения файлов по расширению:
#   rez = sorted(os.listdir(myDir + '/data/sysinfo'))
#   iList = list(filter(lambda x: x.endswith('.sh'), rez))
# iList = glob(myDir + '/data/sysinfo/*.sh') # Вар.1. Отобразить полный путь по маске
# iList = list(glob(os.path.join(myDir + '/data/sysinfo', '*.sh'))) # Вар.2. Отобразить полный путь по маске
# -----| Пример удаления файлов по маске
# import os, glob
# for file in glob.glob('/home/ihor/*.py'):
#    os.remove(file)

import logging
#from aiogram import Bot, Dispatcher, executor, types
from aiogram import Bot, executor, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ParseMode, InputMediaPhoto # последнее для РЕДАКТИРОВАНИЯ ФОТО
from aiogram.utils.markdown import text, bold, italic, code, underline, strikethrough

# async def delete_message(message: types.Message, sleep_time: int = 0): # не пошло)) НЕ УДАЛЯЕТ DICE!!!
#from aiogram.utils.exceptions import (MessageToEditNotFound, MessageCantBeEdited, MessageCantBeDeleted, MessageToDeleteNotFound)
#from contextlib import suppress # Для удаления сообщений Бота !!!! [asyncio.create_task(delete_message(msg, 5))]
import asyncio # await asyncio.sleep(1) # Wait a little

import subprocess # Для запуска скриптов и команд Linux
import os  # для работы с файлами типа: rez = sorted(os.listdir(path))
from glob import glob # Для списка файлов каталога по маске: list(glob(os.path.join(myDir, '*.sh')))
import random # Для создания MediGroup (SEND FILES) случайным образом из 9 фото = БОЛЬШЕ НЕ ПРОХОДИТ! (видимо размер)
from PIL import Image  # Для выделения размера файла width = image.size[0] #Определяем ширину
#import cv2 # Для определения параметров Видео Файла на диске = надо установить через pip3
import json # для работы с данными: json.dump(data, outfile) & data = json.load(json_file)

import time # time.sleep(5)   # Delays for 5 seconds
from datetime import datetime
from pytz import timezone # tz = timezone("Europe/Moscow") -> today = datetime.now(tz) -> iTime = today.strftime("%H:%M:%S")

from myconfig import *
from keyboard import *

PASS = False # Глобальная переменна для проверки кодового слова на входе [def: global PASS] и запуска псевдо-клавиатуры
iKey = ''    # Глобальная переменна для набора пароля на псевдо-клавиатуре
myPass = '🚑💡⏳' # скорая лампочка песочные_часы
iNum = 0
tz = timezone("Europe/Moscow")

uid01 = USER_ID_01          # My Main ID
#uid11 = USER_ID_11          # VVM Main ID
TOKEN = TOKEN_11            # [⚙️ VTI Comp Assistant💡] = vti-monitor {New Bot [27-05-2021] for vvm}
bot = Bot(token=TOKEN)      # Объект бота
dp = Dispatcher(bot)        # Диспетчер для бота
# Configure logging
logging.basicConfig(level=logging.INFO) # Включаем логирование, чтобы не пропустить важные сообщения
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# ========== [ON START UP] ====================]
async def on_startup(dp): # должно быть [executor.start_polling(dp, on_startup=on_startup, skip_updates=False)]
#    return True
#   print ('1 ____ set def com___')
   await set_default_commands(dp) # Устанавливаем дефолтные команды
#   print ('2 ____ start up___')
   await on_startup_notify(dp)    # Бот уведомляет про запуск


# ========== [SET DEFAULT MENU] ===============]
async def set_default_commands(dp):
   await dp.bot.set_my_commands([
      types.BotCommand('help24', 'Вывести справку 💡'),
      types.BotCommand('my_mems', 'Шпаргалка 🗄'),
      types.BotCommand('weather24', 'Прогноз погоды 24ч 🌤'),
      types.BotCommand('games24', 'Relax игры юмор 🎮'),
      types.BotCommand('proxy_vpn', 'Запустить proxy London 📡'),
      types.BotCommand('server_kino', 'Подключить сервер кино 🖥'),
      types.BotCommand('set_vpn', 'Разрешить admin-доступ ssh 🌐'),
      types.BotCommand('open_rdp', 'Разрешить доступ к экрану 🈴'),
      types.BotCommand('admin_bot', 'Запустить бот admin_linux 💎'),
      types.BotCommand('stop_bot', 'Закончить работу бота 📴'),
      types.BotCommand('stop_computer', '0.Выключить компьютер! 🔴'),
   ])

# ========== [ON START UP NOTIFY] =============]
async def on_startup_notify(dp): # Бот уведомляет про запуск всем разрешенным лицам
   for user in ID:
      try:
#         await dp.bot.send_message(user, '⚙️ VTI Comp Assist💡 is ON!')
#         iMsg = '⚙️ *VTI* Comp Assistant 💡:\n *- Жду кодовое слово ...*'
         iMsg = '⚙️ <b>VTI</b> Comp Assistant 💡:&#10; <b>- Жду кодовое слово ...</b>'
         with open(myDir + '/data/00.jpg', 'rb') as photo:
            await bot.send_photo(user, photo, iMsg, parse_mode=ParseMode.HTML, reply_markup=types.ReplyKeyboardRemove())
#            await bot.send_photo(user, photo, iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=types.ReplyKeyboardRemove())
#            await bot.send_photo(ID[0], photo)
#      await message.send_photo(ID[0], photo, caption=MyMsg % message.chat.first_name, parse_mode=ParseMode.MARKDOWN)
      except Exception as err:
         logging.exception(err)


## ========== [DELETE BOT MESSAGES] =============] [ asyncio.create_task(delete_message(msg, 5))]
#async def delete_message(message: types.Message, sleep_time: int = 0):
#   await asyncio.sleep(sleep_time)
#   with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
#      await message.delete()
# не пошло))

## ========== [CLEAN THE SCREEN] =============] [ asyncio.create_task(clean_screen(15))]
async def clean_screen(sleep_time: int = 0): # Очистить экран ПК от сообщений через заданный интервал
   await asyncio.sleep(sleep_time)
   subprocess.call(['/bin/bash', myDir + '/scripts/kill_proc.sh', 'sm'])



# [START] Хэндлер на команду [/1307] = кодовое слово для доступа к Боту
#@dp.message_handler(commands=['1307', 'start'])
@dp.message_handler(commands=['1307'])
async def start_command(message: types.Message): # присваиваем любое название функции
    today = datetime.now(tz)
    iT = today.strftime("%M%S")
    global PASS, iKey
    iKey = ''
    PASS = False
    if str(message.chat.id) in str(ID): # Вывод псевдо-меню доступно только для круга лиц с ID
# ----| Моментально удаляем кодовое слово с экрана!!!! |-----
#       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку) или команду!
# ----| Формируем псевдо-клавиатуру с иконками для ВВОДА ПАРОЛЯ ! |-----
#          папка бумага ципленок замок  лупа
#          зубы  земля  укол     скорая деньги
#          песок счеты  блокнот  компас сфикс
#          клава стекло лампа    почта  авто
       passwd_kb = types.InlineKeyboardMarkup(row_width=5)
       text_and_data = (
          ('...📂...', '#G📂' + iT), ('...🧻...️', '#G🧻' + iT), ('...🐣...', '#G🐣' + iT), ('...🔐...', '#G🔐' + iT), ('...🔎...', '#G🔎' + iT),
          ('...💀...', '#G💀' + iT), ('...🌖...', '#G🌖' + iT), ('...💉...', '#G💉' + iT), ('...🚑...', '#G🚑' + iT), ('...💸...', '#G💸' + iT),
          ('...⏳...', '#G⏳' + iT), ('...🧮...', '#G🧮' + iT), ('...📝...', '#G📝' + iT), ('.🧭.️', '#G🧭' + iT), ('...🗿...', '#G🗿' + iT),
          ('...⌨...️', '#G⌨️' + iT), ('...💎...', '#G💎' + iT), ('...💡...', '#G💡' + iT), ('...📬...', '#G📬'+ iT), ('...🚗...', '#G🚗'+ iT),
       )
       row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
       passwd_kb.add(*row_btns)
       msg = await message.answer(startMsg % message.from_user.first_name, parse_mode=ParseMode.HTML, reply_markup=kb_main_menu)
#       print ('start _______|| ', msg)
       iMsg = '🌚' # Луна
       await message.answer(iMsg, reply_markup=passwd_kb)
#       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
#       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
#       time.sleep(7) # тормозит общий процесс
#       await asyncio.sleep(7) # пауза независимая от ввода пароля)
#       await msg.delete() # Все удаляет, но и клавиатуру тоже)
    else:
       await other_people(message)
#       return True

@dp.callback_query_handler(lambda c: c.data[0:2] == '#G') # ОБРАБОТЧИК INLINE-КНОПОК PASSWD
async def passwd_btn(call: types.CallbackQuery):
    global PASS, iKey, myPass
    PASS = False
    today = datetime.now(tz)
    iT = today.strftime("%M%S")
    cid = call.from_user.id
    if str(cid) in str(ID):
       passwd_kb = types.InlineKeyboardMarkup(row_width=5)
       text_and_data = (
          ('...📂...', '#G📂' + iT), ('...🧻...️', '#G🧻' + iT), ('...🐣...', '#G🐣' + iT), ('...🔐...', '#G🔐' + iT), ('...🔎...', '#G🔎' + iT),
          ('...💀...', '#G💀' + iT), ('...🌖...', '#G🌖' + iT), ('...💉...', '#G💉' + iT), ('...🚑...', '#G🚑' + iT), ('...💸...', '#G💸' + iT),
          ('...⏳...', '#G⏳' + iT), ('...🧮...', '#G🧮' + iT), ('...📝...', '#G📝' + iT), ('.🧭.️', '#G🧭' + iT), ('...🗿...', '#G🗿' + iT),
          ('...⌨...️', '#G⌨️' + iT), ('...💎...', '#G💎' + iT), ('...💡...', '#G💡' + iT), ('...📬...', '#G📬'+ iT), ('...🚗...', '#G🚗'+ iT),
       )
       row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
       passwd_kb.add(*row_btns)
       iMsg = call.data[2]
       await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, reply_markup=passwd_kb)
#    time.sleep(1) # Пауза для анимации значков
       if iMsg == '🗿': # Сфинкс обнуляет счетчик!
          iKey = ''
       else:
          iKey = iKey + iMsg
#    print ('=====|| ', iKey)
       if iKey == myPass:
          PASS = True
#       iMsg = '🌞'
          iMsg = '🌝'
          await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id)
          time.sleep(2)
          iMsg = '♻️  Выбираем задачу:'
          await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id)
#       await bot.edit_message_text(startMsg % call.from_user.first_name, call.from_user.id, call.message.message_id) # Good!!
#       await bot.send_message(startMsg % call.from_user.first_name, call.from_user.id, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_main_menu) #Bad
#       await bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=kb_main_menu) #Bad
    else:
       return True



# +++++++++++++ [MAIN MENU] +++++++++++++++++++++++++] = reply_markup=kb_main_markup # Обработчики Основного фиксированного меню внизу
@dp.message_handler(lambda message: message.text == str(but01.text)) # but01=('💻 SysINFO')   ===== MAIN MENU =====
#async def main_menu_sysinfo(callback_query: types.CallbackQuery):
async def main_menu_sysinfo(message: types.Message):
#    if PASS and str(message.chat.id) in str(ID):
       today = datetime.now(tz)
       iTime = today.strftime("%H:%M:%S")
       iMsg = 'ℹ️ System INFO {' + iTime + '}' + logo
       sysinfo_kb = await make_sysinfo_kb('sysinfo', '#Q') # ===== ВЫЗОВ ФУНКЦИИ СОЗДАНИЯ КНОПОК ИЗ ФАЙЛА ПРИЛОЖЕНИЙ
       await message.answer(iMsg, parse_mode=ParseMode.HTML, reply_markup=sysinfo_kb)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
#       await message.answer('🙈')
#    else:
#       return True



@dp.message_handler(lambda message: message.text == str(but02.text)) # but02=('⌨️  PC Control')   ===== MAIN MENU =====
async def main_menu_pc_control(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
#       await message.answer_dice(emoji="🏀")
       await message.answer(help_pc_control, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_pc_menu)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True



@dp.message_handler(lambda message: message.text == str(but03.text)) # but03=('📤 Send Files')   ===== MAIN MENU =====
async def main_menu_send_files(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
#       await message.answer_dice(emoji="⚽")
       await message.answer(help_send_files, parse_mode=ParseMode.HTML, reply_markup=kb_send_menu, disable_web_page_preview=True)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(lambda message: message.text == str(but04.text)) # but04=('💡HELP')   ===== MAIN MENU =====
async def main_menu_help(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
#       await message.answer_dice(emoji="🎳")
       await message.answer(help_message, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_help_menu)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True

@dp.message_handler(lambda message: message.text == str(but05.text)) # but05=('Tips📍')   ===== MAIN MENU =====
async def main_menu_tips(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
#       await message.answer_dice(emoji="🎳")
       await message.answer(tips_message, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_tips_menu)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(lambda message: message.text == str(but11.text)) # but11=('🏠Smart House 🛁')   ===== MAIN MENU =====
async def main_menu_smart_house(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
#       await message.answer_dice(emoji="🎯")
       await message.answer(help_smart_house, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_smart_menu)
       time.sleep(2) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(lambda message: message.text == str(but14.text)) # but14=('📺DLNA')   ===== MAIN MENU =====
async def main_menu_dlna(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
#       await message.answer_dice(emoji="🎲")
       await message.answer(help_dlna, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_dlna_menu)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True

# End MAIN +++++++++++++++++++++++]



#@dp.message_handler(lambda message: message.text == str(but20.text)) # but20=('↩️ BACK')
@dp.message_handler(lambda message: message.text == str(but20.text)) # but20=('↩️ BACK')   +++++ BACK to MAIN MENU +++++
@dp.message_handler(lambda message: message.text == str(but30.text)) # или but30=('↩️')
async def back1_2main_menu(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       iMsg = '♻️  Выбираем задачу:'
       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_main_menu)
# ---| Моментально удаляем кнопку ОБРАТНО |-----
#       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True



# [1] ---------- Sys INFO --------------]
async def make_sysinfo_kb(Folder, Symb): # Функция создания клавиатуры   +++++ SysINFO +++++
       sysinfo_kb = types.InlineKeyboardMarkup(row_width=3) # ФОРМИРУЕМ КНОПКИ МЕНЮ
       myRow = []
       path = myDir + "/data/" + Folder
       rez = sorted(os.listdir(path))
       iList = list(filter(lambda x: x.endswith('.sh'), rez))
       for item in iList:
          btn = str(item)
          my_text = '🔘 ' + btn.strip('.sh')
          my_data = Symb + btn
          myRow.append(types.InlineKeyboardButton(my_text, callback_data=my_data))
       sysinfo_kb.add(*myRow)
       return sysinfo_kb



@dp.callback_query_handler(lambda c: c.data[0:2] == '#Q') # Обработчик кнопок  but01=('💻 SysINFO') +++++ SysINFO +++++
async def sysinfo_btn(call: types.CallbackQuery):
  if PASS:
     today = datetime.now(tz)
     iTime = today.strftime("%H:%M:%S")
     iScript = call.data.strip('#Q')
# Работающий переход на другое меню! Практически здесь оказалось неудобно, но эффектно
#     if call.data[2] == '8': # По нажатой кнопке [6_Приложения] переходим в меню [SOFT]->[LIST]
##        call.data = '#P0' # [SOFT]->[LIST] ('#P3')->[MANUAL]
#        await list_soft_btn(call) # Запуск Нового Меню ['#P0']->[SOFT]->[LIST]
#     else:
     subprocess.call(['/bin/bash', myDir + '/data/sysinfo/' + iScript]) # Запустить определенный скрипт сбора информации
     iName = iScript.strip('.sh')
     iFile = myDir + '/data/sysinfo/' + iName + '.txt'
     with open(iFile, 'r') as file1: # Собранная Скриптом Инфо записана уже в этот Файл!
        Info = file1.read()
#    iMsg = 'ℹ️ System INFO {' + iTime + '}' + logo
     iMsg = '{' + iTime + '} <b>' + iName + ':</b>\n<code>""""""""""""""""""""""""</code>\n' + Info
     sysinfo_kb = await make_sysinfo_kb('sysinfo', '#Q') # ===== ВЫЗОВ ФУНКЦИИ СОЗДАНИЯ КНОПОК ИЗ ФАЙЛА ПРИЛОЖЕНИЙ
     await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.HTML, reply_markup=sysinfo_kb)

# End Sys INFO --------------]



# [2] ---------- PC Control --------------]
@dp.message_handler(commands=['stop_computer']) # Выключить ПК из Меню Команд
@dp.message_handler(lambda message: message.text == str(but21.text)) # but21=('🔴StopPC')   +++++ PC Control +++++
#async def pc_menu_stop(callback_query: types.CallbackQuery):
async def pc_menu_stop(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       today = datetime.now(tz)
       iTime = today.strftime("%H:%M")
       iMsg = text(
          '<b>[' + iTime + ']</b> Система будет остановлена через 1 мин.',
          '&#10;&#10;⌚️ Отменить по <b>команде</b> терминала: [<code>shutdown -c</code>]',
          '&#10;&#10;👋 <b>До скорой встречи</b> 👋&#10;.'
       )
#       await message.answer(iMsg + logo, parse_mode=ParseMode.HTML)
       with open(myDir + '/data/lenj.png', 'rb') as photo:
#          await bot.send_photo(message.chat.id, photo, iMsg, parse_mode=ParseMode.HTML, reply_markup=types.ReplyKeyboardRemove())
          await bot.send_photo(message.chat.id, photo, iMsg, parse_mode=ParseMode.HTML)
       subprocess.call(['/bin/bash', myDir + '/scripts/shutdown.sh', 'P'])
#       subprocess.call(['DISPLAY=:0', 'gdialog', '--msgbox', '"Система будет остановлена через 1 мин.!"'])
#       subprocess.call(['/usr/bin/sudo', '/usr/sbin/shutdown', '-P', '+1'])
       time.sleep(5) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
       sms = await message.answer('🤓')
       time.sleep(5)
       await bot.delete_message(chat_id=message.chat.id, message_id=sms.message_id) # Удаляем Мартышкину морду)
       sms = await message.answer('🥱')
       time.sleep(4)
       await bot.delete_message(chat_id=message.chat.id, message_id=sms.message_id) # Удаляем Мартышкину морду)
       sms = await message.answer('🧐')
       time.sleep(4)
       await bot.delete_message(chat_id=message.chat.id, message_id=sms.message_id) # Удаляем Мартышкину морду)
       sms = await message.answer('🥺')
       time.sleep(4)
       await bot.delete_message(chat_id=message.chat.id, message_id=sms.message_id) # Удаляем Мартышкину морду)
       sms = await message.answer('😢')
       time.sleep(4)
       await bot.delete_message(chat_id=message.chat.id, message_id=sms.message_id) # Удаляем Мартышкину морду)
       sms = await message.answer('😭')
       time.sleep(4)
       await bot.delete_message(chat_id=message.chat.id, message_id=sms.message_id) # Удаляем Мартышкину морду)
       sms = await message.answer('🙈')
       time.sleep(4)
       await bot.delete_message(chat_id=message.chat.id, message_id=sms.message_id) # Удаляем Мартышкину морду)
       sms = await message.answer('🙀')
       time.sleep(3)
       await bot.delete_message(chat_id=message.chat.id, message_id=sms.message_id) # Удаляем Мартышкину морду)
       sms = await message.answer('😱')
       time.sleep(3)
       await bot.delete_message(chat_id=message.chat.id, message_id=sms.message_id) # Удаляем Мартышкину морду)
       sms = await message.answer('🥶')
       time.sleep(3)
       await bot.delete_message(chat_id=message.chat.id, message_id=sms.message_id) # Удаляем Мартышкину морду)
    else:
       return True


@dp.message_handler(lambda message: message.text == str(but22.text)) # but22=('🔄Reboot')   +++++ PC Control +++++
async def pc_menu_reboot(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
#       await message.answer('*⏱  ждем загрузку ПК ...*', parse_mode=ParseMode.MARKDOWN)
#       await message.answer('*⏱  ждем загрузку ПК ...*', parse_mode=ParseMode.MARKDOWN, show_alert=True) # Ошибка ALERT нут здесь = inline
       await message.answer('*⏱  ждем загрузку ПК ...*', parse_mode=ParseMode.MARKDOWN)
       subprocess.call(['/bin/bash', myDir + '/scripts/shutdown.sh', 'r'])
#       subprocess.call(['/usr/bin/sudo', '/usr/sbin/init', '6'])
#       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(lambda message: message.text == str(but23.text)) # but23=('⚙️  Config')   +++++ PC Control +++++
async def pc_menu_config(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
#       subprocess.call(['/bin/bash', myDir + '/scripts/but23_config.sh'])
#       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_pc_menu)
       today = datetime.now(tz)
       iTime = today.strftime("%H:%M:%S")
       iMsg = '☢️️  CONFIGs {' + iTime + '}'
       my_config_kb = await make_config_kb() # ===== ВЫЗОВ ФУНКЦИИ СОЗДАНИЯ КНОПОК ИЗ ФАЙЛА ПРИЛОЖЕНИЙ
       my_config_kb.row(types.InlineKeyboardButton('🟥 CLOSE ALL CONFIG WONDOWs ❌', callback_data='#Close')) # ДОБАВИТЬ НИЖНИЙ РЯД КНОПОК
#       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=my_config_kb)
       await message.answer(iMsg, parse_mode=ParseMode.HTML, reply_markup=my_config_kb)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(lambda message: message.text == str(but25.text)) # but25=('🈴 WEB')   +++++ PC Control +++++
async def pc_menu_web(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       iPid = subprocess.call(['/bin/bash', myDir + '/scripts/but25_web.sh'])
#       iMsg = 'WEB-сервер на Python3 запущен: ' + str(iPid)
#       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_pc_menu)
#       await message.answer(iMsg, parse_mode=ParseMode.HTML, reply_markup=kb_pc_menu)
       with open(myDir + '/scripts/web.txt', 'r') as file1:
          iMsg = file1.read()
       await message.answer(iMsg, parse_mode=ParseMode.HTML)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(commands=['proxy_vpn']) # Включить/Выключить Proxy-VPN [London] из Меню Команд
@dp.message_handler(lambda message: message.text == str(but29.text)) # but29='📡proxy'   +++++ PC Control +++++
async def pc_menu_proxy(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       subprocess.call(['/bin/bash', myDir + '/scripts/but29_proxy.sh'])
       with open(myDir + '/scripts/but29_proxy.txt', 'r') as file1:
          iMsg = file1.read()
       await message.answer(iMsg, parse_mode=ParseMode.HTML, reply_markup=kb_pc_menu)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(commands=['open_rdp']) # Включить/Выключить VNC [RDP] из Меню Команд
@dp.message_handler(lambda message: message.text == str(but28.text)) # but28='🈴VNC'   +++++ PC Control +++++
async def pc_menu_vnc(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       subprocess.call(['/bin/bash', myDir + '/scripts/but28_vnc.sh'])
       with open(myDir + '/scripts/but28_vnc.txt', 'r') as file1:
          iMsg = file1.read()
       await message.answer(iMsg, parse_mode=ParseMode.HTML, reply_markup=kb_pc_menu)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(commands=['set_vpn']) # Разрешить Администрировать через SSH-VPN из Меню Команд
@dp.message_handler(lambda message: message.text == str(but26.text)) # but26=('🌐 VPN')   +++++ PC Control +++++
async def pc_menu_vpn(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
#       vIP = subprocess.call(['/bin/bash', myDir + '/scripts/but26_vpn.sh']) # Так ничего не передает - нужно сложнее писать
       subprocess.call(['/bin/bash', myDir + '/scripts/but26_vpn.sh'])
#       iMsg = '<b>VPN</b> позволяет удаленный <b>доступ к этому ПК</b>\n⏱ отключится через <b>~20</b> мин автоматически'
       with open(myDir + '/scripts/vpn.txt', 'r') as file1:
          iMsg = file1.read()
#       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_pc_menu)
       await message.answer(iMsg, parse_mode=ParseMode.HTML, reply_markup=kb_pc_menu)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(commands=['admin_bot']) # Запсук Бота admin_linux из Меню Команд
@dp.message_handler(lambda message: message.text == str(but27.text)) # but27=('💎 t.me')   +++++ PC Control +++++
async def pc_menu_tmbot(message: types.Message):
#    subprocess.call(['/usr/bin/python3', '../1.Telegram/admin_linux.py']) # Хороший рабочий вариант, но будет ошибка при повторном запуске
    if PASS and str(message.chat.id) in str(ID):
       subprocess.call(['/bin/bash', myDir + '/scripts/but27_admin.sh'])
       with open(myDir + '/scripts/but27_admin.txt', 'r') as file1:
          iMsg = file1.read()
#    file1 = open('./scripts/but27_admin.txt', 'r')  #|| получим объект файла
#    iMsg = file1.readlines()                        #|| считываем все строки
#    file1.close                                     #|| закрываем файл
#    iMsg = 'Telegram-Bot *admin_linux.py* запущен' + str(iPid) + '!\n[ПЕРЕЙТИ в admin_linux ↗️](t.me/zaq_ki_no1_bot)'
#    await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_pc_menu)
       await message.answer(iMsg, parse_mode=ParseMode.HTML, reply_markup=kb_pc_menu)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True
#@dp.message_handler(lambda message: message.text == str(but28.text)) # but28=('')


async def make_config_kb(): # Функция создания клавиатуры Config из файла    +++++ PC Control +++++
    my_config_kb = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True)  # ФОРМИРУЕМ КНОПКИ МЕНЮ
    subprocess.call(['/bin/bash', myDir + '/scripts/config.sh'])
    file1 = open(myDir + '/scripts/config_2.txt', 'r') # получим объект файла c отметками о запуске ОКОН КОНФИГУРАЦИИ
    lines = file1.readlines() # считываем все строки
    for line in lines: # итерация по строкам
        if (line[0:2] == '1#'): # если уже ЗАПУЩЕНО ПРИЛОЖЕНИЕ
           img = '🟢 '
        else:                   # если еще НЕ ЗАПУЩЕНО ПРИЛОЖЕНИЕ
           img = '⚪️ '
        my_text = img + line[2:].strip()
        my_data = '#C' + line[2:].strip() # !!! Если добавить больше символов - выдает ОШИБКУ!!!
        my_config_kb.row(types.InlineKeyboardButton(my_text, callback_data=my_data))
    file1.close # закрываем файл
    return my_config_kb


@dp.callback_query_handler(lambda c: c.data == '#Close') # For ('🟥 CLOSE ALL CONFIG WONDOWs ❌', callback_data='#Close')
async def close_config_btn(call: types.CallbackQuery):
    today = datetime.now(tz)
    iTime = today.strftime("%H:%M:%S")
    iMsg = '☢️️  CONFIGs {' + iTime + '}'
    subprocess.call(['/bin/bash', myDir + '/scripts/config_close.sh']) # Закрыть разом все Windows (ОКНА НАСТРОЕК)
    my_config_kb = await make_config_kb() # ===== ВЫЗОВ ФУНКЦИИ СОЗДАНИЯ КНОПОК ИЗ ФАЙЛА ПРИЛОЖЕНИЙ
    my_config_kb.row(types.InlineKeyboardButton('🟥 CLOSE ALL CONFIG WONDOWs ❌', callback_data='#Close')) # ДОБАВИТЬ НИЖНИЙ РЯД КНОПОК
#    await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.MARKDOWN, reply_markup=my_config_kb)
    await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.HTML, reply_markup=my_config_kb)


@dp.callback_query_handler(lambda c: c.data[0:2] == '#C') # call = CallbackQuery @ TRIGGER For All CONFIG button   +++++ CONFIG +++++
async def triger_config_btn(call: types.CallbackQuery):
    today = datetime.now(tz)
    iTime = today.strftime("%H:%M:%S")
    cName = call.data.strip('#C')
    iMsg = '☢️  CONFIGs {' + iTime + '}'
    subprocess.call(['/bin/bash', myDir + '/scripts/config_triger.sh', cName.strip()])
    my_config_kb = await make_config_kb() # ===== ВЫЗОВ ФУНКЦИИ СОЗДАНИЯ КНОПОК ИЗ ФАЙЛА ПРИЛОЖЕНИЙ
    my_config_kb.row(types.InlineKeyboardButton('🟥 CLOSE ALL CONFIG WONDOWs ❌', callback_data='#Close')) # ДОБАВИТЬ НИЖНИЙ РЯД КНОПОК
#    await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.MARKDOWN, reply_markup=my_config_kb)
    await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.HTML, reply_markup=my_config_kb)


# End PC Control -------------------------]



# ----------- SEND FILES ----------------]
@dp.message_handler(lambda message: message.text == str(but31.text)) # but31=('📷', '= Photos\n')   +++++ SEND FILES +++++
async def photo_menu_send_files(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       today = datetime.now(tz)
       iTime = today.strftime("%H:%M:%S")
       iMsg = '📷 Photos & Images {' + iTime + '}'
       images_kb = await make_folder_kb('Images', '#I', 3, '.jpg') # ===== ВЫЗОВ ФУНКЦИИ СОЗДАНИЯ КНОПОК ИЗ ФАЙЛА ПРИЛОЖЕНИЙ
#       linux_help_kb.row(types.InlineKeyboardButton('♦️  Media Group ♠️', callback_data='#Igroup')) # Не ясно, как запускать Media в Inline???
#       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=images_kb)
       await message.answer(iMsg, parse_mode=ParseMode.HTML, reply_markup=images_kb)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True

@dp.message_handler(lambda message: message.text == str(but32.text)) # but32=('🎧', '= Sounds\n')   +++++ SEND FILES +++++
async def sound_menu_send_files(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       today = datetime.now(tz)
       iTime = today.strftime("%H:%M:%S")
#       iMsg = '📷 Music & Voice {' + iTime + '}'
       iMsg = '🎧 Music & Voice {' + iTime + '}'
       audio_kb = await make_folder_kb('Voice', '#A', 1, '.mp3') # ===== ВЫЗОВ ФУНКЦИИ СОЗДАНИЯ КНОПОК ИЗ ФАЙЛА ПРИЛОЖЕНИЙ
#       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=audio_kb)
       await message.answer(iMsg, parse_mode=ParseMode.HTML, reply_markup=audio_kb)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True

@dp.message_handler(lambda message: message.text == str(but33.text)) # but33=('📹', '= Videos\n')   +++++ SEND FILES +++++
async def video_menu_send_files(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       today = datetime.now(tz)
       iTime = today.strftime("%H:%M:%S")
       iMsg = '📹 Video & Movies {' + iTime + '}'
       video_kb = await make_folder_kb('Video', '#V', 2, '.mp4') # ===== ВЫЗОВ ФУНКЦИИ СОЗДАНИЯ КНОПОК ИЗ ФАЙЛА ПРИЛОЖЕНИЙ
#       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=video_kb)
       await message.answer(iMsg, parse_mode=ParseMode.HTML, reply_markup=video_kb)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True

@dp.message_handler(lambda message: message.text == str(but34.text)) # but34=('📂', '= PDF/Docs\n')   +++++ SEND FILES +++++
async def document_menu_send_files(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       today = datetime.now(tz)
       iTime = today.strftime("%H:%M:%S")
       iMsg = '🗂  <b>PDF & DOCs</b> {' + iTime + '}'
       document_kb = await make_folder_kb('PDF', '#F', 1, '.pdf') # ===== ВЫЗОВ ФУНКЦИИ СОЗДАНИЯ КНОПОК ИЗ ФАЙЛА ПРИЛОЖЕНИЙ
       await message.answer(iMsg, parse_mode=ParseMode.HTML, reply_markup=document_kb)
       time.sleep(3) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True

@dp.message_handler(lambda message: message.text == str(but35.text)) # but35=('♦️ ♠️', '= Media Group)    +++++ SEND FILES +++++
async def media_group_send_files(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
#       await types.ChatActions.upload_photo() # Good bots should send chat actions = В ЛОГАХ КУЧА ДАННЫХ ПРО КАРТИНКИ!!!
       media = types.MediaGroup() # Create media group
       path = myDir + '/data/Images'
#       rez = sorted(os.listdir(path)) # Много фоток не проходит из-за размера!!! Limit = 20 Mb
       rez = os.listdir(path)
       randSet = random.sample(rez, 8) # GOOD!!! Если подписывать все фото, то не будет внизу общей подписи, а при прокрутке потом будут!
       for imgName in randSet:
#          media.attach_photo(types.InputFile(myDir + '/data/Images/' + imgName), imgName.strip('.jpg')) # Attach local file with all captions
          media.attach_photo(types.InputFile(myDir + '/data/Images/' + imgName)) # Attach local file with NO CAPTION!
       today = datetime.now(tz)
       iDay = today.strftime("%d-%m-%Y")
       myStr = '🔘 <b>MediaGroup</b> до 20 МБ из 9 random Фото [<b>' + iDay + '</b>]'
#       media.attach_photo(types.InputFile(myDir + '/data/tiger.jpg'), caption=myStr, parse_mode=ParseMode.HTML) # Нужно для ОБЩЕЙ ПОДПИСИ ВНИЗУ!
       myFoto = 'AgACAgIAAxkBAAIsTmDhiermX32mM6sx9K7d5RWQDCq4AAK9tjEbcfIJS4Eo5xK_1KtZAQADAgADeAADIAQ'
       media.attach_photo(myFoto, caption=myStr, parse_mode=ParseMode.HTML) # Нужно для ОБЩЕЙ ПОДПИСИ ВНИЗУ!
       await message.answer_media_group(media=media) ### Done! Send media group
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True

# Выдает ошибку: [aiogram.utils.exceptions.TypeOfFileMismatch: Type of file mismatch]
#@dp.message_handler(lambda message: message.text == str(but36.text)) # but36 =('🔮') # VideoNote
#async def video_note(message: types.Message):
#    if PASS and str(message.chat.id) in str(ID):
#       path = myDir + '/data/Video/'
#       rez = os.listdir(path)
#       randNote = random.choice(rez)
#       print ('-------| ', randNote)
#       VideoNote = "BQACAgIAAxkBAAIg52DY5BOkGv-hp6H9zb9qmo4zKYtJAAL4DgAC0enJSvCJWVB3eGeaIAQ"
#       VideoNote = "BAACAgIAAxkBAAIhD2DZlftoFm3RsWD1Ljp7MS6WTpntAAKIDgACN_LISlGPr0FwMP1dIAQ"
#       VideoNote = "BAACAgIAAxkBAAIhFmDZlqAwxRL0kYUHDtzwwod4aVx3AAKKDgACN_LISuw__6Nmyzl9IAQ"
#       await message.answer_video_note(video_note=VideoNote) # Отправка VideoNote по ID
#       myFile = path + randNote
#       await message.answer_video_note(path + randNote)
#       with open(myFile, 'rb') as File:
#          await bot.send_video_note(message.chat.id, File)
#    else:
#       return True




# НЕ ПОШЛО - НУЖНО ЗНАТЬ, КАК ЗАПУСКАТЬ [await bot.send_media_group(x,y,z)] = параметры???
#@dp.callback_query_handler(lambda c: c.data == '#Igroup') # CallbackQuery #('♦️  Media Group ♠️', '#Igroup')  +++++ SEND FILES +++++
#async def media_group_btn(call: types.CallbackQuery):
#       await types.ChatActions.upload_photo() # Good bots should send chat actions
#       media = types.MediaGroup() # Create media group
#       path = myDir + '/data/Images'
#       rez = sorted(os.listdir(path))
#       for imgName in rez:
#          media.attach_photo(types.InputFile(myDir + '/data/Images/' + imgName), imgName.strip('.jpg')) # Attach local file
##       await message.answer_media_group(media=media) ### Done! Send media group
#       await bot.send_media_group(call.from_user.id, media=media) ### Done! Send media group

@dp.callback_query_handler(lambda c: c.data[0:2] == '#I') # ОБРАБОТЧИК INLINE-КНОПОК but31=('📷', '= Photos\n')   +++++ SEND FILES +++++
async def images_btn(call: types.CallbackQuery):
    if PASS and str(call.message.chat.id) in str(ID): # ВАЖНО = call.message.chat.id !!!
       sName = call.data.strip('#I')
#       images_kb = await make_folder_kb('Images', '#I', 3, '.jpg') # ===== ВЫЗОВ ФУНКЦИИ СОЗДАНИЯ КНОПОК ИЗ ФАЙЛА ПРИЛОЖЕНИЙ
#       img = Image.open(myDir + '/data/Images/' + sName)
#       width = img.size[0]  # Определяем ширину. Метод для .JPG
#       height = img.size[1] # Определяем высоту. Метод для .JPG
#       iMsg = '📷' + sName + ' 📐 ' + str(width) + ' x ' + str(height)
#       await bot.send_photo(call.from_user.id, img, '📷' + sName, parse_mode=ParseMode.MARKDOWN, reply_markup=images_kb)
#       Img = Image.open(myDir + '/data/Images/' + myName)
       myName = str(sName.strip())
       zDir = myDir + '/data/Images/' + myName
       Img = Image.open(zDir)
       Width = str(Img.size[0])  # Определяем ширину. Метод для .JPG
       Height = str(Img.size[1])  # Определяем ширину. Метод для .JPG
#       iMsg = '📷' + myName + ' 📐<b>' + Width.strip() + 'x' + Height.strip() + '</b>' # Выводить нельзя [_] в имени, ибо разметка MARKDOWN!!!
       iMsg = '🔘 ' + myName + ' 📐<b>' + Width.strip() + 'x' + Height.strip() + '</b>' # Выводить нельзя [_] в имени, ибо разметка MARKDOWN!!!
       with open(zDir, 'rb') as img: # Вывод надписи под рисунком!!!
#       with open(myDir + '/data/Images/' + sName, 'rb') as img: # Вывод надписи под рисунком!!!
#          await bot.send_photo(call.from_user.id, img, iMsg, parse_mode=ParseMode.MARKDOWN_V2) # V2 не проходит с [.] в расширении файла
          await bot.send_photo(call.from_user.id, img, iMsg, parse_mode=ParseMode.HTML) # ВАРИАНТ БЕЗ ЗАГРУЗКИ KB
#          await bot.send_photo(call.from_user.id, img, iMsg) # ВАРИАНТ БЕЗ ЗАГРУЗКИ KB
       await bot.answer_callback_query(call.id, text=zDir) # &&&-----| ВЫВОДИТ ВРЕМЕННО КОРОТКОЕ СООБЩЕНИЕ НА ЭКРАН!!! |------&&&
    else:
       return True



@dp.callback_query_handler(lambda c: c.data[0:2] == '#F') # ОБРАБОТЧИК INLINE-КНОПОК but34=('📂', '= PDF/Docs\n')  +++++ SEND FILES +++++
async def pdf_document_btn(call: types.CallbackQuery):
    if PASS and str(call.message.chat.id) in str(ID): # ВАЖНО = call.message.chat.id !!!
       sName = call.data.strip('#F')
#       iMsg = 'PDF: ' + str(sName)
       with open(myDir + '/data/PDF/' + sName, 'rb') as DOCs: #
          await bot.send_document(call.from_user.id, DOCs) # ВАРИАНТ БЕЗ ЗАГРУЗКИ KB
    else:
       return True


@dp.callback_query_handler(lambda c: c.data[0:2] == '#A') # ОБРАБОТЧИК INLINE-КНОПОК but32=('🎧', '= Sounds\n')   +++++ SEND FILES +++++
async def voice_btn(call: types.CallbackQuery): # ПРИ СОЗДАНИИ КНОПОК ВАЖНО КОНТРОЛИРОВАТЬ ДЛИННУ ФАЙЛОВ !!!
    if PASS and str(call.message.chat.id) in str(ID): # ВАЖНО = call.message.chat.id !!!
       today = datetime.now(tz)
       iDay = today.strftime("%d.%m.%Y")
       sName = call.data.strip('#A')
       myTit = sName.split('-')[0]
       myPerf = sName.partition('-')[2]
       myCap = '🎼 <b>' + iDay + '</b> 🎶'
       myThumb = open(myDir + '/data/flag.jpg', 'rb')
#       iMsg = 'PDF: ' + str(sName)
       with open(myDir + '/data/Voice/' + sName, 'rb') as File: # ЗДЕСЬ ЛУЧШЕ ИСПОЛЬЗОВАТЬ ИМЕННО AUDIO вместо VOICE!!!
          await bot.send_audio(call.from_user.id, File, caption=myCap, performer=myPerf, title=myTit, thumb=myThumb, parse_mode=ParseMode.HTML) # ВАРИАНТ БЕЗ ЗАГРУЗКИ KB
       myThumb.close()
    else:
       return True


@dp.callback_query_handler(lambda c: c.data[0:2] == '#V') # ОБРАБОТЧИК INLINE-КНОПОК VIDEO!!!   +++++ SEND FILES +++++
async def video_btn(call: types.CallbackQuery): # ПРИ СОЗДАНИИ КНОПОК ВАЖНО КОНТРОЛИРОВАТЬ ДЛИННУ ФАЙЛОВ !!!
    if PASS and str(call.message.chat.id) in str(ID): # ВАЖНО = call.message.chat.id !!!
       today = datetime.now(tz)
       iDay = today.strftime("%y-%m-%d")
       sName = call.data.strip('#V')
#       myTit = sName.split('-')[0]
#       myPerf = sName.partition('-')[2]
#       myCap = '🎼 <b>' + iDay + '</b> 🎶'
#       myThumb = open(myDir + '/data/flag.jpg', 'rb')
#       iMsg = 'PDF: ' + str(sName)
       myFile = myDir + '/data/Video/' + sName
#       vid = cv2.VideoCapture(myFile)
#       height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
#       width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
       iMsg = '🔘 ' + sName
       with open(myFile, 'rb') as File:
          await bot.send_video(call.from_user.id, File, caption=iMsg)
#       with open(myDir + '/data/Video/' + sName, 'rb') as File: #
#          await bot.send_video(call.from_user.id, File) #
#       myThumb.close()
    else:
       return True

#import cv2
#file_path = "./video.avi"
#vid = cv2.VideoCapture( file_path )
#height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
#width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)


# SEND FILES ----------------]



# [4] ---------- HELP & TIPs --------------]
@dp.message_handler(lambda message: message.text == str(but41.text)) # but41=('🐧linux')   +++++ HELP & TIPs +++++
async def help_menu_linux(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       today = datetime.now(tz)
       iTime = today.strftime("%H:%M:%S")
       iMsg = '🐧 Linux Manuals {' + iTime + '}'
       linux_help_kb = await make_folder_kb('linux', '#L', 2, '.txt') # ===== ВЫЗОВ ФУНКЦИИ СОЗДАНИЯ КНОПОК ИЗ ФАЙЛА ПРИЛОЖЕНИЙ
       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=linux_help_kb)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


async def make_folder_kb(Folder, Symb, Width, Mime): # Функция создания клавиатуры софта чтением приложений из файла # but41=('🐧linux') KEYBOARD ⌨️
##    ls = subprocess.Popen(["ls", "-p", "."], stdout=subprocess.PIPE)                        # define the ls command
#    ls = subprocess.Popen(["ls", myDir + "/data/" + Folder], stdout=subprocess.PIPE)         # define the ls command
#    grep = subprocess.Popen(["grep", "-v", "/$"], stdin=ls.stdout, stdout=subprocess.PIPE)  # define the grep command
#    endOfPipe = grep.stdout                                # read from the end of the pipe (stdout)
#    print (endOfPipe) # Метод не очень хороший = дает косяки [b'basic.txt']
#    for line in endOfPipe:                                 # output the files line by line
#        print (line.strip()) # = [b'basic.txt']??
#
    my_new_kb = types.InlineKeyboardMarkup(row_width=Width)  # ФОРМИРУЕМ КНОПКИ МЕНЮ
    myRow = []
    path = myDir + "/data/" + Folder
    rez = sorted(os.listdir(path))
    for item in rez:
        btn = str(item.strip())
#        my_text = '✏️ ' + btn.strip('.txt')
        my_text = '📓 ' + btn.strip(Mime)
        my_data = Symb + btn # !!! Если добавить больше символов - выдает ОШИБКУ!!!
        myRow.append(types.InlineKeyboardButton(my_text, callback_data=my_data))
#        my_linux_kb.row(types.InlineKeyboardButton(my_text, callback_data=my_data)) # Создает только один ряд кнопок
    my_new_kb.add(*myRow)
    return my_new_kb


@dp.message_handler(lambda message: message.text == str(but42.text)) # but42=('💎 t_me')   +++++ HELP & TIPs +++++
async def help_menu_t_me(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       await message.answer(about_tme, parse_mode=ParseMode.HTML, reply_markup=kb_help_menu, disable_web_page_preview=True)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(lambda message: message.text == str(but43.text)) # but43=('📺dlna')   +++++ HELP & TIPs +++++
async def help_menu_dlna(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       with open(myDir + '/data/dlna.jpg', 'rb') as img:
#          await message.answer_photo(img)
#       await message.answer(about_dlna, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_help_menu)
          await message.answer_photo(img, about_dlna, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_dlna_menu)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(lambda message: message.text == str(but44.text)) # but44=('👮 jobs')   +++++ HELP & TIPs +++++
async def help_menu_jobs(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       with open(myDir + '/data/00.jpg', 'rb') as img: # Вывод надписи под рисунком!!!
          await message.answer_photo(img, about_jobs, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_help_menu)
#          await message.answer_photo(img) # Раньше эти две команды работали в паре, но отдельно выводили
#       await message.answer(about_jobs, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_help_menu)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(lambda message: message.text == str(but45.text)) # but45=('📰 news')   +++++ HELP & TIPs +++++
async def help_menu_news(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       await message.answer(about_news, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_help_menu, disable_web_page_preview=True)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(lambda message: message.text == str(but46.text)) # but46=('📎 links')   +++++ HELP & TIPs +++++
async def help_menu_links(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       await message.answer(about_links, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_help_menu)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(lambda message: message.text == str(but47.text)) # but47=('🛠tools')   +++++ HELP & TIPs +++++
async def help_menu_others(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
#       await message.answer(about_others, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_help_menu)
       with open(myDir + '/data/00.jpg', 'rb') as img: # Вывод надписи под рисунком!!!
          await message.answer_photo(img, about_others, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_help_menu)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(commands=['my_mems']) # Вызов ШПАРГАЛКИ (в виде картинок) из Меню Команд
@dp.message_handler(lambda message: message.text == str(but48.text)) # but48=('🗄files')   +++++ HELP & TIPs +++++
async def help_menu_file(message: types.Message):
    global iNum
    if PASS and str(message.chat.id) in str(ID):
       today = datetime.now(tz)
       iT = today.strftime("%M%S")
       with open(myDir + '/data/files.json') as json_file:
          data = json.load(json_file)
          iMax = len(data['image']) # подсчет элементов JSON
          iNum = random.randint(0, iMax-1)
          Str = data['image'][iNum]['about']
          id = data['image'][iNum]['id']
          file_id = data['image'][iNum]['file_id']
#       iMsg = 'Всего: ' + str(iMax) + '\nНомер: ' + str(iNum+1) + '\n🔘 ' + Str # Good Test!!!
#       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=job_files_menu)
#       iMsg = '🔘 <code>' + Str + '</code>'
       iMsg = '⚓️ Шпаргалка с полезными записями и формулами'
       job_files_menu = types.InlineKeyboardMarkup(row_width=3)
#          ('⏪start', '#JS' + iT), ('LIST', '#JA' + iT), ('⏩end', '#JE' + iT),
       text_and_data = (
          ('< LEFT ⏮', '#JL' + iT), (id, '#JAM' + id + iT), ('⏭ RIGHT >', '#JR' + iT),
          ('● START ⏪', '#JS' + iT), (' ⏩ END ●', '#JE' + iT),
       )                                            # ====| Псевдо-кнопка для декорации ШИРИНЫ КАРТИНОК
#       iBtn = '====================================++++++++++'
       iBtn = '🔘 ' + Str + ' {' + data['image'][iNum]['file_name'] + '}'
       job_files_menu.add(types.InlineKeyboardButton(text=iBtn, callback_data='#JAR' + iT))
       row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
       job_files_menu.add(*row_btns)
       await message.answer_photo(file_id, caption=iMsg, parse_mode=ParseMode.HTML, reply_markup=job_files_menu)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


#@dp.callback_query_handler(lambda c: c.data[0:3] == '#JA') # ОБРАБОТЧИК +++ RANDOM +++++ HELP & TIPs +++++
@dp.callback_query_handler(lambda c: c.data[0:2] == '#J') # ОБРАБОТЧИК +++ RANDOM +++++ HELP & TIPs +++++
async def file_list_btn(call: types.CallbackQuery):
    global iNum
    today = datetime.now(tz)
    iT = today.strftime("%M%S")
    with open(myDir + '/data/files.json') as json_file:
       data = json.load(json_file)
       iMax = len(data['image']) # подсчет элементов JSON
       if call.data[0:4] == '#JAR':
          iNum = random.randint(0, iMax-1)
       elif call.data[0:4] == '#JAM':
          iNum = iMax//2 # Деление без остатка или # iNum = round(iMax/2-1)
       elif call.data[0:3] == '#JS':
          iNum = 0
       elif call.data[0:3] == '#JE':
          iNum = iMax-1
       elif call.data[0:3] == '#JL':
          iNum = iNum-1
       elif call.data[0:3] == '#JR':
          if iNum == iMax-1:
             iNum = 0
          else:
             iNum = iNum+1
       Str = data['image'][iNum]['about']
       id = data['image'][iNum]['id']
       file_id = data['image'][iNum]['file_id']
    iMsg = '🔘 <code>' + Str + '</code>'
    job_files_menu = types.InlineKeyboardMarkup(row_width=3)
#       ('⏮left', '#JL' + iT), (id, '#J' + id + iT), ('⏭right', '#JR' + iT),
#       ('⏪start', '#JS' + iT), ('LIST', '#JA' + iT), ('⏩end', '#JE' + iT),
    text_and_data = (
       ('< LEFT ⏮', '#JL' + iT), (id, '#JAM' + id + iT), ('⏭ RIGHT >', '#JR' + iT),
       ('● START ⏪', '#JS' + iT), (' ⏩ END ●', '#JE' + iT),
    )
#    iBtn = '====================================++++++++++'
#    iBtn = '🔘 ' + Str
    iBtn = '🔘 ' + Str + ' {' + data['image'][iNum]['file_name'] + '}'
    job_files_menu.add(types.InlineKeyboardButton(text=iBtn, callback_data='#JAR' + iT))
#    job_files_menu.add(types.InlineKeyboardButton(text='====================================++++++++++', callback_data='#JAR' + iT))
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    job_files_menu.add(*row_btns)
#    await bot.edit_message_media(call.id, InputMediaPhoto(file_id)) # VER.1
#    await bot.edit_message_media(call.from_user.id, call.message.message_id, InputMediaPhoto(file_id))
#
# ---| ПОЛУЧИЛАСЬ ПРЫГАЮЩАЯ РАБОЧАЯ СХЕМА 8-) # VER.2
#    await bot.edit_message_media(media=photo_media, chat_id=call.message.chat.id, message_id=call.message.message_id)
#    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=job_files_menu)
#
    photo_media = InputMediaPhoto(file_id) # VER.3 Меняется только картинка без текста!
    await bot.edit_message_media(media=photo_media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=job_files_menu)



@dp.callback_query_handler(lambda c: c.data[0:2] == '#L') # ОБРАБОТЧИК INLINE-КНОПОК LINUX MANUALS  +++++ HELP & TIPs +++++
async def linux_help_btn(call: types.CallbackQuery):
    today = datetime.now(tz)
    iTime = today.strftime("%H:%M:%S")
    sName = call.data.strip('#L')
#    print(sName)
#    iMsg = '+++ Нажата ' + str(sName.strip()) + ' кнопка'
#    with open(myDir + '/data/linux/' + sName, 'r') as file1:
    zDir = myDir + '/data/linux/' + sName
    with open(zDir, 'r') as file1:
       iManual = file1.read()
    iMsg = '🐧*' + str(sName.strip('.txt')) + '* {' + iTime + '} \n++++++++++++++++++++++\n' + iManual
    linux_help_kb = await make_folder_kb('linux', '#L', 2, '.txt') # ===== ВЫЗОВ ФУНКЦИИ СОЗДАНИЯ КНОПОК ИЗ ФАЙЛА ПРИЛОЖЕНИЙ
    await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.MARKDOWN, reply_markup=linux_help_kb)
    await bot.answer_callback_query(call.id, text=zDir) # &&&-----| ВЫВОДИТ ВРЕМЕННО КОРОТКОЕ СООБЩЕНИЕ НА ЭКРАН!!! |------&&&

# End HELP & TIPs -------------------------]



# [5] ---------- SMART HOUSE --------------]
@dp.message_handler(lambda message: message.text == str(but50.text)) # but50=('🌡📈')   +++++ SMART HOUSE +++++
async def cpu_temp(message: types.Message): # Прототип работающей функции ВЫВОДА ГРАФИКА ЦПУ методом скриншота
    if PASS and str(message.chat.id) in str(ID):
       iMsg = '🌡 CPU Temp: <b>43.8 ℃ </b>'
       with open(myDir + '/data/grafik.jpg', 'rb') as img: # Вывод надписи под рисунком!!!
          await message.answer_photo(img, iMsg, parse_mode=ParseMode.HTML, reply_markup=kb_smart_menu)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(lambda message: message.text == str(but94.text)) # ('💊') # Аптечка в дорогу
async def apteka_btn(message: types.Message): # Аналог вывода рабочих документов с кнопками прокрутки готовых картинок из памяти
#    if PASS and str(message.chat.id) in str(ID):
#       media = types.MediaGroup() # Create media group
       today = datetime.now(tz)
       iT = today.strftime("%M%S")
       with open(myDir + '/data/apteka.json') as json_file:
          data = json.load(json_file)
          iMax = len(data['apteka']) # подсчет элементов JSON
          iNum = random.randint(0, iMax-1)
          Str = data['apteka'][iNum]['about']
          id = data['apteka'][iNum]['id']
          file_id = data['apteka'][iNum]['file_id']
          fSize = data['apteka'][iNum]['file_size']
#       iMsg = '🔘 <code>' + Str + '</code> [<b>' + str(iNum+1) + '</b>]'
#       iMsg = '🔘 <code>' + Str + '</code>&#10;' + id + ' [<b>' + fSize + '</b>] {' + today.strftime("%d-%m-%Y_%H:%M") + '}'
       iMsg = '🔘 <code>' + Str + '</code>'
       dopInfo = '=' + id + '= размер файла в байтах: [' + fSize + '] {' + today.strftime("%d-%m-%Y_%H:%M") + '}'
       apteka_menu = types.InlineKeyboardMarkup(row_width=7)
       text_and_data = (
          ('1️⃣', '#E1' + iT), ('2️⃣', '#E2' + iT), ('3️⃣', '#E3' + iT), ('4️⃣', '#E4' + iT),
          ('5️⃣', '#E5' + iT), ('6️⃣', '#E6' + iT), ('7️⃣', '#E7' + iT),
       )
       apteka_menu.add(types.InlineKeyboardButton(text=dopInfo, callback_data='#E0'))
       row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
       apteka_menu.add(*row_btns)
       await message.answer_photo(file_id, caption=iMsg, parse_mode=ParseMode.HTML, reply_markup=apteka_menu) # GOOD!! но править лучше MtdiaGroup
#       media.attach_photo(file_id, caption=iMsg, parse_mode=ParseMode.HTML) # Нужно для ОБЩЕЙ ПОДПИСИ ВНИЗУ!
#       await message.answer_media_group(media=media) ### Done! Send media group = NO reply_markup!!!
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
#    else:
#       return True


@dp.callback_query_handler(lambda c: c.data[0:2] == '#E') # ОБРАБОТЧИК КНОПОК [1-7] ПОД КАРТИНКАМИ apteka
async def apteka_btn(call: types.CallbackQuery):
#    if PASS and str(call.message.chat.id) in str(ID): # ВАЖНО = call.message.chat.id !!!
       today = datetime.now(tz)
       iT = today.strftime("%M%S")
#       sName = call.data.strip('#E')
#       iNum = int(sName.strip())-1
       if call.data[2] == '0':
          iNum = random.randint(0,6)
       else:
          iNum = int(call.data[2])-1
#       print ('mems &&&&===| ', call.data[2], ' = ', iNum) # ?! Была плавающая проблема с 0 адресом (т.е. iNum=1-1)?!
       with open(myDir + '/data/apteka.json') as json_file:
          data = json.load(json_file)
          Str = data['apteka'][iNum]['about']
          id = data['apteka'][iNum]['id']
          file_id = data['apteka'][iNum]['file_id']
          fSize = data['apteka'][iNum]['file_size']
#       iMsg = '🔘 <code>' + Str + '</code> [<b>' + str(iNum+1) + '</b>]'
#       iMsg = '🔘 <code>' + Str + '</code>&#10;' + id + ' [<b>' + fSize + '</b>] {' + today.strftime("%d-%m-%Y_%H:%M") + '}'
       iMsg = '🔘 <code>' + Str + '</code>'
       dopInfo = '=' + id + '= размер файла в байтах: [' + fSize + '] {' + today.strftime("%d-%m-%Y_%H:%M") + '}'
       apteka_menu = types.InlineKeyboardMarkup(row_width=7)
       text_and_data = (
          ('1️⃣', '#E1' + iT), ('2️⃣', '#E2' + iT), ('3️⃣', '#E3' + iT), ('4️⃣', '#E4' + iT),
          ('5️⃣', '#E5' + iT), ('6️⃣', '#E6' + iT), ('7️⃣', '#E7' + iT),
       )
       apteka_menu.add(types.InlineKeyboardButton(text=dopInfo, callback_data='#E0'))
       row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
       apteka_menu.add(*row_btns)
#       media = types.MediaGroup() # Create media group # НЕ ПОШЛО!!!
#       print ('XZ =====|| ', media) # Выдает [] пустоту
#       media.attach_photo(file_id, caption=iMsg, parse_mode=ParseMode.HTML) # Нужно для ОБЩЕЙ ПОДПИСИ ВНИЗУ! НЕ ПОШЛО!!!
#       await bot.edit_message_media(media=media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=apteka_menu) # BAD!
       myMedia=InputMediaPhoto(file_id, caption=iMsg, parse_mode=ParseMode.HTML)
#       myMedia=InputMediaPhoto(file_id) # ВСЕ ОТЛИЧНО, НО ТОЛЬКО КАРТИНКА!
       await bot.edit_message_media(media=myMedia, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=apteka_menu)
#    else:
#       return True




@dp.message_handler(commands=['weather24']) # Вывод Прогноза погоды на 24 часа из Меню Команд
@dp.message_handler(lambda message: message.text == str(but95.text)) # but95=('🌦погода')   +++++ SMART HOUSE +++++
async def weather_moscow(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       subprocess.call(['/usr/bin/python3', myDir + '/scripts/10_weather_mos.py']) # Хороший рабочий вариант
       with open(myDir + '/scripts/moscow.txt', 'r') as file1:
          iMsg = file1.read()
#       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_tips_menu)
       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(lambda message: message.text == str(but96.text)) # ('📸ipCam') # Отправка фото с IP-Cam
async def ipcam_btn(message: types.Message):
#    subprocess.call(['/bin/bash', myDir + '/scripts/ip_cam.sh']) # запускаем камеру IP-Cam = текущий кадр
    today = datetime.now(tz)
    iDay = today.strftime("%y-%m-%d_%H:%M")
    iMsg = '🔘 фото с ip-cam [<b>' + str(iDay) + '</b>]'
    if PASS and str(message.chat.id) in str(ID):
       with open(myDir + '/data/10.jpg', 'rb') as img: # Вывод надписи под кадром с камеры (или default img)
          await message.answer_photo(img, iMsg, parse_mode=ParseMode.HTML, reply_markup=kb_tips_menu)
       time.sleep(2) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True



@dp.message_handler(lambda message: message.text == str(but97.text)) # but97=('робот')   +++++ SMART HOUSE +++++
async def robot_menu(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       btn_robot_kb = types.InlineKeyboardMarkup(row_width=3, size=2)
       text_and_data = (
          ('️🕞 Timer', '#Rtimer'), ('⬆ FORWARD️', '#Rforward'), ('🔎 Search', '#Rsearch'),
          ('⬅ LEFT️️', '#Rleft'), ('☢ TURN️', '#Rturn'), ('RIGHT ➡️', '#Rright'),
          ('📣 Sound', '#Rsound'), ('⬇️ BACKWARD', '#Rbackward'), ('📸 Image', '#Rimage'),
       )
       row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
#       btn_robot_kb.row(*row_btns) # все в один ряд выстроились (горизонтально)
       btn_robot_kb.add(*row_btns)
       iMsg = '📗 Инструкция 🤖:\n⬅️️ влево    ➡️ вправо\n⬆️ вперед   ⬇️ назад\n*.. в разработке* ⚡'
       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=btn_robot_kb)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(lambda message: message.text == str(but92.text)) # but92=('🆔Телеграм')   +++++ SMART HOUSE +++++
async def tme_id(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       await message.answer_dice(emoji="🎲")
       iMsg = 'Работающий здесь Telegram ID: *[' + str(message.chat.id) + ']*'
       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(commands=['games24']) # Запуск из меню
@dp.message_handler(lambda message: message.text == str(but58.text)) # ('игры')   +++++ SMART HOUSE +++++
async def games_menu(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       Link1 = 'https://yandex.ru/games/play/101956/?app-id=101956&utm_medium=search&utm_source=yandex&utm_campaign=rus_games_general-igra-bezkav_desk_yandex_search_460.new%7C59207592&utm_term=%D0%B8%D0%B3%D1%80%D0%B0%20%D0%B2%20%D0%B1%D1%80%D0%B0%D1%83%D0%B7%D0%B5%D1%80%D0%B5%20%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D1%8B%D0%B5#app-id=101956&catalog-session-uid=catalog-274bb297-920c-502f-86f8-72a4b664c7cd-1626092089129-6c0e&rtx-reqid=4123413581283176182&pos=%7B%22listType%22%3A%22categorized%22%2C%22tabCategory%22%3A%22common%22%7D'
       Link2 = 'https://yandex.ru/games/play/98912/?app-id=98912&utm_source=game_popup_menu#app-id=98912&catalog-session-uid=catalog-bb9b98af-4099-53bf-a9c7-1abb15a4c939-1626176775063-7cb5&rtx-reqid=2316179384837023145&pos=%7B%22listType%22%3A%22suggested%22%2C%22tabCategory%22%3A%22common%22%7D'
       today = datetime.now(tz)
       iT = today.strftime("%M%S")
#       games_kb = types.InlineKeyboardMarkup(row_width=7, size=2)
       games_kb = types.InlineKeyboardMarkup(row_width=7) # футбол баскетбол автомат боулинг дартс dice
       text_and_data = (
          ('⚽️', '#Y⚽️' + iT), ('🏀', '#Y🏀' + iT), ('🎰', '#Y🎰' + iT), ('🎳', '#Y🎳' + iT),
          ('🎯', '#Y🎯' + iT), ('🎲', '#Y🎲' + iT), ('.🏆.', '#Y0' + iT),
          ('🚂Train', '#Y1' +iT), ('Matrix', '#Y2' +iT), ('🔥aFire', '#Y3' +iT), ('☯Судьба', '#Y4' +iT),
       )
       row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
       games_kb.add(*row_btns)
       games_kb.add(types.InlineKeyboardButton('♟Шашки', url=Link1))
       games_kb.insert(types.InlineKeyboardButton('Морской Бой🔫', url=Link2))
       iMsg = '🤪' # crazy face
       msg = await message.answer(iMsg)
       time.sleep(2) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       iMsg = 'Испытай свою <b>Удачу</b> ✌️'
       await message.answer(iMsg, parse_mode=ParseMode.HTML, reply_markup=games_kb)
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
       await msg.delete() # Удаляем прыгающую РОЖУ) = crazy face
    else:
       return True



@dp.callback_query_handler(lambda c: c.data[0:2] == '#Y') # ОБРАБОТЧИК INLINE-КНОПОК...
async def dice_btn(call: types.CallbackQuery):
  if PASS:
    Link1 = 'https://yandex.ru/games/play/101956/?app-id=101956&utm_medium=search&utm_source=yandex&utm_campaign=rus_games_general-igra-bezkav_desk_yandex_search_460.new%7C59207592&utm_term=%D0%B8%D0%B3%D1%80%D0%B0%20%D0%B2%20%D0%B1%D1%80%D0%B0%D1%83%D0%B7%D0%B5%D1%80%D0%B5%20%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D1%8B%D0%B5#app-id=101956&catalog-session-uid=catalog-274bb297-920c-502f-86f8-72a4b664c7cd-1626092089129-6c0e&rtx-reqid=4123413581283176182&pos=%7B%22listType%22%3A%22categorized%22%2C%22tabCategory%22%3A%22common%22%7D'
    Link2 = 'https://yandex.ru/games/play/98912/?app-id=98912&utm_source=game_popup_menu#app-id=98912&catalog-session-uid=catalog-bb9b98af-4099-53bf-a9c7-1abb15a4c939-1626176775063-7cb5&rtx-reqid=2316179384837023145&pos=%7B%22listType%22%3A%22suggested%22%2C%22tabCategory%22%3A%22common%22%7D'
    today = datetime.now(tz)
    iT = today.strftime("%M%S")
    iDay = today.strftime("%d-%m-%y")
    iTime = today.strftime("%H:%M:%S")
    games_kb = types.InlineKeyboardMarkup(row_width=7)
    text_and_data = (
       ('⚽️', '#Y⚽️' + iT), ('🏀', '#Y🏀' + iT), ('🎰', '#Y🎰' + iT), ('🎳', '#Y🎳' + iT),
       ('🎯', '#Y🎯' + iT), ('🎲', '#Y🎲' + iT), ('.🏆.', '#Y0' + iT),
       ('🚂Train', '#Y1' +iT), ('Matrix', '#Y2' +iT), ('🔥aFire', '#Y3' +iT), ('☯Судьба', '#Y4' +iT),
    )
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    games_kb.add(*row_btns)
    games_kb.add(types.InlineKeyboardButton('♟Шашки', url=Link1))
    games_kb.insert(types.InlineKeyboardButton('Морской Бой🔫', url=Link2))
#    iMsg = 'Испытай свою <b>Удачу</b> ✌️'
#    iSH = {'train':'games_train.sh', 'matrix':'games_matrix.sh', 'xx':'games_xx.sh', 'yy':'games_yy.sh'}
#    msg = {'train':'🚂 <b>Поезд Ту-ту..</b>', 'matrix':'🕷', 'xx':'⚡️', 'yy':'☃️'}
    iSH = {'1':'games_train.sh', '2':'games_matrix.sh', '3':'games_fire.sh', '4':'games_fortune.sh'}
    msg = {'1':'🚂 <b>Поезд Ту-ту..</b>', '2':'🕷', '3':'⚡️', '4':'☃️'}
    iGame = call.data[2]
    if iGame in ('1', '2', '3'): # '🚂train', 'matrix', 'aFire'
#       iMsg = '🚂 <b>Поезд Ту-ту..</b>'
       iMsg = msg[iGame]
       await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.HTML, reply_markup=games_kb)
       subprocess.call(['/bin/bash', myDir + '/scripts/' + iSH[iGame]]) # запускаем выбранный скрипт с шюткой на экране)
#    elif iGame == '3':
#       Link = 'https://yandex.ru/games/play/101956/?app-id=101956&utm_medium=search&utm_source=yandex&utm_campaign=rus_games_general-igra-bezkav_desk_yandex_search_460.new%7C59207592&utm_term=%D0%B8%D0%B3%D1%80%D0%B0%20%D0%B2%20%D0%B1%D1%80%D0%B0%D1%83%D0%B7%D0%B5%D1%80%D0%B5%20%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D1%8B%D0%B5#app-id=101956&catalog-session-uid=catalog-274bb297-920c-502f-86f8-72a4b664c7cd-1626092089129-6c0e&rtx-reqid=4123413581283176182&pos=%7B%22listType%22%3A%22categorized%22%2C%22tabCategory%22%3A%22common%22%7D'
#       iMsg = '♟ <a href="' + Link + '">ШАШКИ в БРАУЗЕРЕ</a>'
#       await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.HTML, reply_markup=games_kb)
    elif iGame == '4':
#       subprocess.call(['/bin/bash', myDir + '/scripts/games_fortune.sh']) # запускаем выбранный скрипт с шюткой на экране)
       subprocess.call(['/bin/bash', myDir + '/scripts/' + iSH[iGame]]) # запускаем выбранный скрипт с шюткой на экране)
       with open(myDir + '/scripts/fortune.txt', 'r') as file:
          data = file.read()
       iMsg = '☯️ <b>Глас Фортуны</b> ⚛️\n' + data
       await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.HTML, reply_markup=games_kb)
#       time.sleep(10)
#       subprocess.call(['/bin/bash', myDir + '/scripts/kill_proc.sh', 'sm'])
       asyncio.create_task(clean_screen(15))
    elif iGame == '0':
       with open(myDir + '/data/dice.txt', 'r') as file:
#          data = file.readlines()[-10:]
#          iMsg = '⛳ <b>Кол-во ОЧКОВ:</b>&#10;' + str(data)
          data = file.readlines()
          tail = data[-10:]
          iMsg = '⛳ <b>Кол-во ОЧКОВ:</b>&#10;' + ''.join(tail)
       await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.HTML, reply_markup=games_kb)
    else: # Здесь запускаются все игры типа Dice
       await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id) # !!! это удаляет старое сообщение с меню
       msg = await bot.send_dice(emoji=iGame, chat_id=call.from_user.id)
       time.sleep(3)
       iVal = str(msg.dice.value) # Кол-во очков (везде до 6, в рулетку - до 64)
       with open(myDir + '/data/dice.txt', 'a') as file: # Записываем для истории все свои достижения по времени и дате [w]=обнуляет начало файла!
          file.write('<b>' + iDay + '</b>_' + iTime + '  ' + iGame + ' <b>' + iVal + '</b>\n')
       iMsg = '⛳️ <b>Кол-во ОЧКОВ:  ' + iVal + ' ' + iGame + '</b>'
       CID = str(call['from']['id'])
       msg = await bot.send_message(chat_id=CID, text=iMsg, parse_mode=ParseMode.HTML) # str(call['from']['id']) !!!===@@@===!!!
       time.sleep(2)
       await games_menu(msg) # после удаления Инлайн-Кнопок Принудитльно запускаем новое МЕНЮ под DICE
#       await games_menu(call.message) # после удаления Инлайн-Кнопок Принудитльно запускаем новое МЕНЮ под DICE
# тесты:
#    await bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=games_kb) # НЕ ЯСЕН РЕЗУЛЬТАТ РАБОТЫ)
#    await bot.edit_message_text(iGame, call.from_user.id, call.message.message_id, parse_mode=ParseMode.MARKDOWN, reply_markup=games_kb)
#    await bot.edit_message_dice(emoji=iGame, call.from_user.id, call.message.message_id, reply_markup=games_kb)
#    iGame = call.data.strip('#Y')
#    print ('--------| ', call.message)   # msg_id = call.message.message_id
#    print ('--------| ', msg.dice.value) # Печатает кол-во выпавших очков (для рулетки max=64)
#    time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
#    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id) # !!! это удаляет само сообщение с меню
#    await bot.delete_message(chat_id=call.from_user.id, message_id=msg.message_id) # !!! Ошибка: не удаляет сам Dice
#    await msg.delete() # не позволяет удалить!
#    await asyncio.create_task(delete_message(msg, 5)) # не позволяет удалить! Сама функция в начале программы!
  else:
    return True



@dp.message_handler(lambda message: message.text == str(but51.text)) # ('🚰🛁')
@dp.message_handler(lambda message: message.text == str(but52.text)) # ('🔌')
@dp.message_handler(lambda message: message.text == str(but53.text)) # ('💡')
@dp.message_handler(lambda message: message.text == str(but54.text)) # ('🔐')
@dp.message_handler(lambda message: message.text == str(but55.text)) # ('🏠окна')
@dp.message_handler(lambda message: message.text == str(but56.text)) # ('🚪двери')
@dp.message_handler(lambda message: message.text == str(but57.text)) # ('⚡реле')
async def time_btn(message: types.Message):
   if PASS:
      time.sleep(3) # пауза для красоты перед удалением "правого смс" на экране от пользователя
      await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
      return True
   else:
     return True

# End SMART HOUSE --------------]




# [6] ---------- SOFT --------------]
@dp.message_handler(lambda message: message.text == str(but12.text)) # but12=('💾 Soft')   +++++ SOFT +++++
async def main_menu_programs(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       today = datetime.now(tz)
       iTime = today.strftime("%H:%M:%S")
       my_soft_kb = await make_soft_kb() # ===== ВЫЗОВ ФУНКЦИИ СОЗДАНИЯ КНОПОК ИЗ ФАЙЛА ПРИЛОЖЕНИЙ
       text_and_data = (('🟡 START ALL', '#P1'), ('💡 MANUAL', '#P3'), ('🔴 STOP ALL', '#P2'))
       row_btns = (types.InlineKeyboardButton(text, callback_data=data, resize_keyboard=True) for text, data in text_and_data) # ДОБАВИЛ RESIZE!!!
       my_soft_kb.row(*row_btns)
       iMsg = '📝 Приложения {' + iTime + '}'
#       with open(myDir + '/data/00.jpg', 'rb') as img: # Вывод надписи под рисунком!!!
#          await message.answer_photo(img, iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=my_soft_kb)
       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=my_soft_kb)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.callback_query_handler(lambda c: c.data == '#P0') # call = CallbackQuery 🌐🌐🌐 For button ('📝 LIST', '#P0')   +++++ SOFT +++++
async def list_soft_btn(call: types.CallbackQuery):
    today = datetime.now(tz)
    iTime = today.strftime("%H:%M:%S")
    my_soft_kb = await make_soft_kb() # ===== ВЫЗОВ ФУНКЦИИ СОЗДАНИЯ КНОПОК ИЗ ФАЙЛА ПРИЛОЖЕНИЙ
    text_and_data = (('🟡 START ALL', '#P1'), ('💡 MANUAL', '#P3'), ('🔴 STOP ALL', '#P2'))
    row_btns = (types.InlineKeyboardButton(text, callback_data=data, resize_keyboard=True) for text, data in text_and_data)
    my_soft_kb.add(*row_btns)
    iMsg = '📝 Приложения {' + iTime + '}'
    await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.MARKDOWN, reply_markup=my_soft_kb)


async def make_soft_kb(): # Функция создания клавиатуры софта чтением приложений из файла
    subprocess.call(['/bin/bash', myDir + '/scripts/soft_list.sh'])
    my_soft_kb = types.InlineKeyboardMarkup(row_width=3)
    file1 = open(myDir + '/scripts/list_all.txt', 'r') # получим объект файла
    lines = file1.readlines() # считываем все строки
    for line in lines: # итерация по строкам
        if (line[0:2] == '1#'): # если уже ЗАПУЩЕНО ПРИЛОЖЕНИЕ
           img = '🟢 ️'
        else:                   # если еще НЕ ЗАПУЩЕНО ПРИЛОЖЕНИЕ
           img = '⚪ '
        my_text = img + line[2:]
        my_data = '#P' + line[2:] # !!! Если добавить больше символов - выдает ОШИБКУ!!!
#        my_soft_kb.add(types.InlineKeyboardButton(my_text, callback_data=my_data))
        my_soft_kb.row(types.InlineKeyboardButton(my_text, callback_data=my_data))
    file1.close # закрываем файл
    return my_soft_kb


@dp.callback_query_handler(lambda c: c.data == '#P3') # call = CallbackQuery 🌐🌐🌐 For button ('💡 MANUAL', '#P3')   +++++ SOFT +++++
async def man_soft_btn(call: types.CallbackQuery):
    my_soft_kb = types.InlineKeyboardMarkup(row_width=3)
    text_and_data = (('🟡 START ALL', '#P1'), ('📝 LIST', '#P0'), ('🔴 STOP ALL', '#P2'))
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    my_soft_kb.row(*row_btns)
    await bot.edit_message_text(help_soft, call.from_user.id, call.message.message_id, parse_mode=ParseMode.MARKDOWN, reply_markup=my_soft_kb)


@dp.callback_query_handler(lambda c: c.data == '#P1') # call = CallbackQuery 🌐🌐🌐 For button ('🟡 START ALL', '#P1')   +++++ SOFT +++++
async def start_soft_btn(call: types.CallbackQuery):
    today = datetime.now(tz)
    iTime = today.strftime("%H:%M:%S")
    subprocess.call(['/bin/bash', myDir + '/scripts/soft_start.sh'])
#    await bot.answer_callback_query(call.id, text='⛑ ВСЕ ПРИЛОЖЕНИЯ\nОСТАНОВЛЕНЫ! ⛔', show_alert=True) # Доп.смс до 200 символов на экран!
    my_soft_kb = await make_soft_kb() # ===== ВЫЗОВ ФУНКЦИИ СОЗДАНИЯ КНОПОК ИЗ ФАЙЛА ПРИЛОЖЕНИЙ
    text_and_data = (('🟡 START ALL', '#P1'), ('💡 MANUAL', '#P3'), ('🔴 STOP ALL', '#P2'))
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    my_soft_kb.add(*row_btns)
    iMsg = '📝 Приложения {' + iTime + '}'
    await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.MARKDOWN, reply_markup=my_soft_kb)

@dp.callback_query_handler(lambda c: c.data == '#P2') # call = CallbackQuery 🌐🌐🌐 For button ('🔴 STOP ALL', '#P2')
async def stop_soft_btn(call: types.CallbackQuery):
    today = datetime.now(tz)
    iTime = today.strftime("%H:%M:%S")
    subprocess.call(['/bin/bash', myDir + '/scripts/soft_stop.sh']) # ЗАПУСКАЕМ ОСТАНОВ ВСЕХ ЗАПУЩЕННЫХ ПРОГРАММ ПО СПИСКУ
#    return True
    await bot.answer_callback_query(call.id, text='⛑ ВСЕ ПРИЛОЖЕНИЯ\nОСТАНОВЛЕНЫ! ⛔️', show_alert=False) # Доп.смс до 200 символов на экран!
    my_soft_kb = await make_soft_kb() # ===== ВЫЗОВ ФУНКЦИИ СОЗДАНИЯ КНОПОК ИЗ ФАЙЛА ПРИЛОЖЕНИЙ
    text_and_data = (('🟡 START ALL', '#P1'), ('💡 MANUAL', '#P3'), ('🔴 STOP ALL', '#P2'))
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    my_soft_kb.add(*row_btns)
    iMsg = '📝 Приложения {' + iTime + '}'
    await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.MARKDOWN, reply_markup=my_soft_kb)


@dp.callback_query_handler(lambda c: c.data[0:2] == '#P') # call = CallbackQuery @ TRIGGER For All SOFT button   +++++ SOFT +++++
async def triger_soft_btn(call: types.CallbackQuery):
    today = datetime.now(tz)
    iTime = today.strftime("%H:%M:%S")
    sName = call.data.strip('#P')
    subprocess.call(['/bin/bash', myDir + '/scripts/soft_triger.sh', sName.strip()])
    my_soft_kb = await make_soft_kb() # ===== ВЫЗОВ ФУНКЦИИ СОЗДАНИЯ КНОПОК ИЗ ФАЙЛА ПРИЛОЖЕНИЙ
    text_and_data = (('🟡 START ALL', '#P1'), ('💡 MANUAL', '#P3'), ('🔴 STOP ALL', '#P2'))
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    my_soft_kb.add(*row_btns)
    iMsg = '📝 Приложения {' + iTime + '}'
    await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.MARKDOWN, reply_markup=my_soft_kb)

# End SOFT --------------]


# [7] ---------- KINO --------------]
@dp.message_handler(lambda message: message.text == str(but13.text)) # but13=('📽 KINO')   +++++ KINO +++++
async def main_menu_kino(message: types.Message): # Запускает первое меню: Список кино из папки MAIN
    if PASS and str(message.chat.id) in str(ID):
       subprocess.call(['/bin/bash', myDir + '/scripts/kino_main_list.sh'])
       my_kino_kb = types.InlineKeyboardMarkup(row_width=3)
       zDir = '/mnt/SSD/iKINO/MAIN'
       file1 = open(myDir + '/data/Kino_Main_List.txt', 'r') # получим объект файла
       lines = file1.readlines() # считываем все строки
       for line in lines: # итерация по строкам
           my_text = '🔘 ️' + line.strip()
           my_data = '#K' + line.strip() # !!! Если добавить больше символов - выдает ОШИБКУ!!!
           my_kino_kb.add(types.InlineKeyboardButton(my_text, callback_data=my_data))
       file1.close # закрываем файл
##       btn_kino_kb.add(types.InlineKeyboardButton('aiogram source', url='https://github.com/aiogram/aiogram')) # OK!
### Дополнительное меню управления Кино !!! Good!
       text_and_data = (('📁 MAIN', '#D1'), ('📁 izYoutube', '#D2'))
       row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
       my_kino_kb.row(*row_btns)
       today = datetime.now(tz)
       iTime = today.strftime("%H:%M:%S")
       iMsg = '📁1.*MAIN:* {' + iTime + '}'
       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=my_kino_kb)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


# ------ ЗАПУСК ВИДЕО ---------] 🌐🌐🌐 ЭТОТ МЕТОД ТОЛЬКО ДЛЯ INLINE-клавиатуры ("плавающей")
#@dp.callback_query_handler(lambda c: c.data and c.data == '#K') # ------ ОБРАБОТЧИК ЗАПУСКА ВИДЕО ПО НАЖАТИЮ КНОПОК С ФИЛЬМАМИ
#async def my_kino_kb_callback_buttons(callback_query: types.CallbackQuery):
#@dp.callback_query_handler(lambda call: True) # !!!!!! Good
@dp.callback_query_handler(lambda c: c.data[0:2] == '#K') # !!!!!! Good   +++++ KINO +++++
async def my_kino_kb_callback_buttons(call: types.CallbackQuery): # call = CallbackQuery 🌐🌐🌐 https://core.telegram.org/bots/api#callbackquery
#    code = call.from_user # {"id": 408372130, "is_bot": false, "first_name": "Дмитрий", "last_name": "Панфилов", "username": "dnp_gtt", "language_code": "ru"}
#    code = call.message # GOOD = Full Info for all Buttons !!!
#    code = "Ок! Запускаю.." + call.message.text # Good - Вывод верхнее сообщение
    code = call.data # Ok! Good = Выдает название нажатой кнопки со спец.символами '#K'
    my_str = code.strip('#K')
    newDir = call.message.text[1:2]
    logger.debug('The Index is %r', newDir)
    subprocess.call(['/bin/bash', myDir + '/scripts/start_vlc.sh', my_str, newDir])
#    if newDir == '1':
#       zDir = '/mnt/SSD/iKINO/MAIN'
#    else:
#       zDir = '/mnt/SSD/iKINO/izYoutube'
    with open(myDir + '/scripts/.vlc.info', 'r') as file1: # .vlc.info
       iMsg = file1.read()
#       vlcPult = file1.read()
#    iMsg = '📽  Запущен файл:&#10;<b>' + my_str + '</b>&#10;' + vlcPult # GOOD!!! [&#10;]=перевод на новую строку
#    subprocess.call(['/bin/bash', myDir + '/scripts/volume.sh', '85'], shell=True) # 0=mute, 1=volume- [-5%], 2=volume+ [+5%], other=unmute..%
    subprocess.call(['/bin/bash', myDir + '/scripts/volume.sh', '85']) # 0=mute, 1=volume- [-5%], 2=volume+ [+5%], other=unmute..%
    with open(myDir + '/scripts/volume.txt', 'r') as file2: # Volume
       iZvuk = file2.readline()
    btn_kino_kb = types.InlineKeyboardMarkup(row_width=3)
    text_and_data = (('📁 MAIN', '#D1'), ('⏹ STOP [VLC]', '#Svlc'), ('📁 izYoutube', '#D2'))
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    btn_kino_kb.row(*row_btns)
    text_and_data = (('🔽 Volume -', '#Z1'), (str(iZvuk), '#Z0'), ('🔼 Volume +', '#Z2'))
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    btn_kino_kb.row(*row_btns)
    await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.HTML, reply_markup=btn_kino_kb)


# ----------- Обработка папок = Вывод списка Кино папки MAIN или izYoutube
@dp.callback_query_handler(lambda c: c.data[0:2] == '#D') # ('📁 MAIN', '#D1') ('📁 izYoutube', '#D2')   +++++ KINO +++++
#@dp.callback_query_handler(lambda c: c.data and c.data == '#D') # Обработка, если слодержит "#D" ('📁 MAIN', '#D1') ('📁 izYoutube', '#D2')
async def folder_kino_btns(call: types.CallbackQuery):
    code = call.data # Ok! Good = Выдает название нажатой кнопки со спец.символами '#S'
    my_str = code.strip('#D')
    today = datetime.now(tz)
    iTime = today.strftime("%H:%M:%S")
#    iMsg = '📁1. *MAIN:* {' + iTime + '}'
    if my_str == '2':
       zDir = '/mnt/SSD/iKINO/izYoutube'
       iMsg = '📁2.*izYoutube:* {' + iTime + '}'
       myScr = myDir + '/scripts/kino_izyoutube_list.sh'
       myList = myDir + '/data/Kino_izYoutube_List.txt'
    else: #    elif my_str == '1':
       zDir = '/mnt/SSD/iKINO/MAIN'
       iMsg = '📁1.*MAIN:* {' + iTime + '}'
       myScr = myDir + '/scripts/kino_main_list.sh'
       myList = myDir + '/data/Kino_Main_List.txt'
    subprocess.call(['/bin/bash', myScr])
    my_kino_kb = types.InlineKeyboardMarkup(row_width=2)
    file1 = open(myList, 'r') # получим объект файла
    lines = file1.readlines() # считываем все строки
    for line in lines: # итерация по строкам
        my_text = '🔘 ️' + line.strip()
        my_data = '#K' + line.strip() # !!! Если добавить больше символов - выдает ОШИБКУ!!!
        my_kino_kb.add(types.InlineKeyboardButton(my_text, callback_data=my_data))
    file1.close # закрываем файл
    text_and_data = (('📁 MAIN', '#D1'), ('📁 izYoutube', '#D2'))
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    my_kino_kb.row(*row_btns)
    await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.MARKDOWN, reply_markup=my_kino_kb)


@dp.callback_query_handler(lambda c: c.data[0:2] == '#Z') # ('🔽 Volume -', '#Z1'), ('🔼 Volume +', '#Z2')   +++++ KINO +++++
async def folder_kino_btns(call: types.CallbackQuery):
    code = call.data # Ok! Good = Выдает название нажатой кнопки со спец.символами '#S'
    my_str = code.strip('#Z')
    today = datetime.now(tz)
    iTime = today.strftime("%H:%M:%S")
    with open(myDir + '/scripts/.vlc.info', 'r') as file1: # .vlc.info
       iMsg = file1.read()
#       vlcPult = file1.read()
#    iMsg = '📽  Запущен файл:&#10;<b>' + my_str + '</b>&#10;' + vlcPult # GOOD!!! [&#10;]=перевод на новую строку
#    iMsg = '🕰 {' + iTime  + '}'
#    subprocess.call(['/bin/bash', myDir + '/scripts/volume.sh', my_str], shell=True) # 0=mute, 1=volume- [-5%], 2=volume+ [+5%], other=unmute..%
    subprocess.call(['/bin/bash', myDir + '/scripts/volume.sh', my_str]) # 0=mute, 1=volume- [-5%], 2=volume+ [+5%], other=unmute..%
    with open(myDir + '/scripts/volume.txt', 'r') as file2: # Volume
       iZvuk = file2.readline() # прочитать первую строку
    btn_kino_kb = types.InlineKeyboardMarkup(row_width=3)
    text_and_data = (('📁 MAIN', '#D1'), ('⏹ STOP [VLC]', '#Svlc'), ('📁 izYoutube', '#D2'))
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    btn_kino_kb.row(*row_btns)
    text_and_data = (('🔽 Volume -', '#Z1'), (str(iZvuk), '#Z0'), ('🔼 Volume +', '#Z2'))
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    btn_kino_kb.row(*row_btns)
    await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.HTML, reply_markup=btn_kino_kb)
#    await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.MARKDOWN, reply_markup=my_kino_kb)


@dp.callback_query_handler(lambda c: c.data == '#Svlc') # call = CallbackQuery 🌐🌐🌐 For STOP [VLC] buttons   +++++ KINO +++++
async def stop_vlc_btn(call: types.CallbackQuery): # call = CallbackQuery 🌐🌐🌐 https://core.telegram.org/bots/api#callbackquery
#    subprocess.call(['/bin/bash', myDir + '/scripts/volume.sh', '0']) # 0=mute, 1=volume- [-5%], 2=volume+ [+5%], other=unmute..%
#    with open(myDir + '/scripts/volume.txt', 'r') as file2: # Volume
#       iZvuk = file2.readline() # прочитать первую строку
#    btn_kino_kb = types.InlineKeyboardMarkup(row_width=3)
#    text_and_data = (('📁 MAIN', '#D1'), ('⏹ STOP [VLC]', '#Svlc'), ('📁 izYoutube', '#D2'))
#    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
#    btn_kino_kb.row(*row_btns)
#    text_and_data = (('🔽 Volume -', '#Z1'), (str(iZvuk), '#Z0'), ('🔼 Volume +', '#Z2'))
#    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
#    btn_kino_kb.row(*row_btns)
#    code = call.data # Ok! Good = Выдает название нажатой кнопки со спец.символами '#S'
#    my_str = code.strip('#S')
#    subprocess.call(['/bin/bash', myDir + '/scripts/kill_proc.sh', my_str])
    subprocess.call(['/bin/bash', myDir + '/scripts/kill_proc.sh', 'vlc'])
    iMsg = '☠️ *VLC Player is stoped!*'
    await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.MARKDOWN)
    time.sleep(1)   # Delays for 1 second
    today = datetime.now(tz)
    iTime = today.strftime("%H:%M:%S")
    zDir = '/mnt/SSD/iKINO/MAIN'
    iMsg = '📁1.*MAIN:* {' + iTime + '}'
    myScr = myDir + '/scripts/kino_main_list.sh'
    myList = myDir + '/data/Kino_Main_List.txt'
    subprocess.call(['/bin/bash', myScr])
    my_kino_kb = types.InlineKeyboardMarkup(row_width=2)
    file1 = open(myList, 'r') # получим объект файла
    lines = file1.readlines() # считываем все строки
    for line in lines: # итерация по строкам
        my_text = '🔘 ️' + line.strip()
        my_data = '#K' + line.strip() # !!! Если добавить больше символов - выдает ОШИБКУ!!!
        my_kino_kb.add(types.InlineKeyboardButton(my_text, callback_data=my_data))
    file1.close # закрываем файл
    text_and_data = (('📁 MAIN', '#D1'), ('📁 izYoutube', '#D2'))
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    my_kino_kb.row(*row_btns)
    await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.MARKDOWN, reply_markup=my_kino_kb)



#@dp.callback_query_handler(lambda c: c.data and c.data == '#S') # call = CallbackQuery 🌐🌐🌐 For all [STOP] buttons
@dp.callback_query_handler(lambda c: c.data[0:2] == '#S') # call = CallbackQuery 🌐🌐🌐 For all [STOP] buttons   +++++ KINO +++++
async def soft_kb_callback_buttons(call: types.CallbackQuery): # call = CallbackQuery 🌐🌐🌐 https://core.telegram.org/bots/api#callbackquery
    code = call.data # Ok! Good = Выдает название нажатой кнопки со спец.символами '#S'
    my_str = code.strip('#S')
    subprocess.call(['/bin/bash', myDir + '/scripts/kill_proc.sh', my_str])
    iMsg = '*[' + my_str + '] is stoped!*'
    await bot.edit_message_text(iMsg, call.from_user.id, call.message.message_id, parse_mode=ParseMode.MARKDOWN, reply_markup=btn_kino_kb)

# End KINO --------------]



# [8] ---------- DLNA --------------]
@dp.message_handler(lambda message: message.text == str(but81.text)) # but81=('🆗 Status')   +++++ DLNA +++++
async def dlna_status(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       subprocess.call(['/bin/bash', myDir + '/scripts/but80_dlna.sh', 'status'])
       with open(myDir + '/scripts/but80_dlna.txt', 'r') as file1:
          iMsg = file1.read()
       await message.answer(iMsg, parse_mode=ParseMode.HTML, reply_markup=kb_dlna_menu)
#       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
#       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(lambda message: message.text == str(but82.text)) # but82=('🔠 D.Base')   +++++ DLNA +++++
async def dlna_force_reload(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       subprocess.call(['/bin/bash', myDir + '/scripts/but80_dlna.sh', 'force-reload'])
       iMsg = '📺*DLNA*:\nБаза данных *медиа* со всех дисков обновляется, процесс может занять от *2 сек до неск. мин*!'
       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_dlna_menu)
       await dlna_status(message)
#       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
#       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True

@dp.message_handler(commands=['server_kino']) # Запуск Сервера Кино из Меню Команд (слева внизу)
@dp.message_handler(lambda message: message.text == str(but83.text)) # but83=('🆕 Server')   +++++ DLNA +++++
async def dlna_server(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       subprocess.call(['/bin/bash', myDir + '/scripts/start_kino.sh'])
       subprocess.call(['/bin/bash', myDir + '/scripts/but80_dlna.sh', 'restart'])
#    with open('./scripts/but83_server.txt', 'r') as file1:
#       iMsg = file1.read()
       iMsg = '📺*DLNA*:\nИдет проверка подключения *Remote-Server*!\nВидео в каталогах:\n*[~/MOSCOW/Video/..]*'
       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_dlna_menu)
       await dlna_status(message)
#       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
#       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(lambda message: message.text == str(but84.text)) # but84=('🆙 Start')   +++++ DLNA +++++
async def dlna_start(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       subprocess.call(['/bin/bash', myDir + '/scripts/but80_dlna.sh', 'start'])
       iMsg = '📺*DLNA*:\nСервис запущен, база данных Кино обновляется!'
       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_dlna_menu)
       await dlna_status(message)
#       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
#       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(lambda message: message.text == str(but85.text)) # but85=('🔄 Reload')   +++++ DLNA +++++
async def dlna_restart(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       subprocess.call(['/bin/bash', myDir + '/scripts/but80_dlna.sh', 'restart'])
       iMsg = '📺*DLNA*:\nСервис в процессе обновления!'
       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_dlna_menu)
       await dlna_status(message)
#       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
#       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True


@dp.message_handler(lambda message: message.text == str(but86.text)) # but86=('⏹  STOP')   +++++ DLNA +++++
async def dlna_restart(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       subprocess.call(['/bin/bash', myDir + '/scripts/but80_dlna.sh', 'stop']) # Там же fusermount -u $HOME/MOSCOW
       iMsg = '📺*DLNA*:\nСервис остановлен, связь с *Remote-Server* разорвана!'
       await message.answer(iMsg, parse_mode=ParseMode.MARKDOWN, reply_markup=kb_dlna_menu)
       await dlna_status(message)
#       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
#       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True

# End ---------- DLNA --------------]



@dp.message_handler(commands=['help24'])
async def process_help_command(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
# Тестовый вывод MediaGroup # GOOD!!
#       await asyncio.sleep(1) # Wait a little
#       await types.ChatActions.upload_photo() # Good bots should send chat actions
#       media = types.MediaGroup() # Create media group
#       media.attach_photo(types.InputFile(myDir + '/data/Images/0bg.jpg'), 'Best BackGround!') # Attach local file
#       media.attach_photo(types.InputFile(myDir + '/data/Images/city.jpg'), 'City') # More local files
#       media.attach_photo(types.InputFile(myDir + '/data/Images/berezy.jpg'), 'Russian Trees') # More local files
#       media.attach_photo(types.InputFile(myDir + '/data/Images/lake.jpg'), 'Lake') # More local files
#       media.attach_photo(types.InputFile(myDir + '/data/Images/house.jpg'), 'house') # More local files
#       media.attach_photo(types.InputFile(myDir + '/data/Images/moscow.jpg'), 'Moscow') # More local files
#       media.attach_photo(types.InputFile(myDir + '/data/Images/tuman.jpg'), 'Tuman') # More local files
#       media.attach_photo(types.InputFile(myDir + '/data/Images/mountains.jpg'), 'Mountains') # More local files
#       await message.answer_media_group(media=media) ### Done! Send media group
#
#       await message.answer(help_command, parse_mode=ParseMode.MARKDOWN)
#       await message.answer(help_command, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
# С картинкой узкое сообещение получается))
#       with open(myDir + '/data/menu.jpg', 'rb') as img:
#          await message.answer_photo(img, help_command, parse_mode=ParseMode.HTML)
       await message.answer(help_command, parse_mode=ParseMode.HTML, disable_web_page_preview=True)
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True



@dp.message_handler(commands=['off', 'stop', 'by', 'stop_bot']) # все команды запускаются со слэшом [/stop], а перечисляются без слэша [/]
async def command_stop(message):
    global PASS
    if PASS and str(message.chat.id) in str(ID):
       reply_text = "Пока!"
#       await message.reply(reply_text, reply_markup=types.ReplyKeyboardRemove())
       await message.reply(reply_text, reply_markup=types.ReplyKeyboardRemove())
       time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
       # with message, we send types.ReplyKeyboardRemove() to hide the keyboard
       PASS = False
    else:
       return True



@dp.message_handler(content_types=['photo'])
async def save_photo(message):
    if PASS and str(message.chat.id) in str(ID):
       today = datetime.now(tz)
       iDay = today.strftime("%y%m%d")
#       t_name = today.strftime("%y%m%d_%H%M%S")
       try:
#          file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
#          file_id = message.photo[-1].file_id
#          downloaded_file = bot.download_file(file_info.file_path)
#          myFile = myDir + '/data/Images/' + file_info.file_path
#          myFile = myDir + '/data/Images/' + 'test.jpg' # GOOD!!
#          myFile = myDir + '/data/Images/' + t_name + '.jpg'
#          with open(myFile, 'wb') as new_file:
#             new_file.write(downloaded_file)
#          file_info = await bot.get_file(message.photo[-1].file_id)
#          await message.photo[-1].download(myFile)
#          await message.reply("Фото добавлено: " + myFile)
          file_id = message.photo[-1].file_id # Получаем File ID, по кот. можем вызвать файл из облака очень быстро в этом>
          file_info = await bot.get_file(file_id) # JSON данные по файлу
          path = file_info.file_path # название файла вида: documents/file_25.docx
#          myFile = myDir + '/data/Images/' + iDay + '-' + str(path.strip('photos/')) # полный путь нового файла: [_] не использовать из-за MARKDOWN!
          myFile = myDir + '/data/Images/' + iDay + '-' + str(path.strip('photos/')) # полный путь нового файла: [_] не использовать из-за MARKDOWN!
          await bot.download_file(path, myFile)
          iW = message.photo[-1].width
          iH = message.photo[-1].height
          iS = message.photo[-1].file_size
#          with open(myFile, 'w') as new_file: # 'wb' дает ошибку!!!
#             new_file.write(bot.download_file(file_info.file_path))
          Width = '● <b>width:</b> <i>' + str(iW) + '</i>&#10;'
          Height = '● <b>height:</b>  <i>' + str(iH) + '</i>&#10;'
          Size = '● <b>file_size:</b>  <i>' + str(iS) + '</i>&#10;'
          FileID = '● <b>file_id:</b> <code>' + file_id + '</code>'
          iMsg = '✅ <u>Файл сохранен</u>:&#10;<code>' + myFile + '</code>&#10;' + Width + Height + Size + FileID
          await message.answer(iMsg, parse_mode=ParseMode.HTML)
          time.sleep(7) # пауза для красоты перед удалением "правого смс" на экране от пользователя
          await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
       except Exception as error: # Обработчик Ошибок Превышения размера файла!
          iMsg = 'ℹ️ <b>' + str(error) + '!</b>&#10;&#10;⛔ Файл превышает лимит в 20 Мбайт.&#10;💰 <b>Приобретайте коммерческую версию!</b>'
          await message.answer(iMsg, parse_mode=ParseMode.HTML)
          time.sleep(7) # пауза для красоты перед удалением "правого смс" на экране от пользователя
          await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True



@dp.message_handler(content_types=['video'])
async def save_photo(message):
    if PASS and str(message.chat.id) in str(ID):
       today = datetime.now(tz)
       iDay = today.strftime("%y-%m-%d")
       try:
          file_id = message.video.file_id # Получаем File ID, по кот. можем вызвать файл из облака очень быстро в этом Боте
          file_info = await bot.get_file(file_id) # JSON данные по файлу
          file_name = message.video.file_name # Получаем "родное" имя файла *.mp4
          if file_name == None:
             file_name = file_info.file_path.strip('videos/')
          myFile = myDir + '/data/Video/' + str(file_name) # полный путь нового файла:
          path = file_info.file_path # название файла вида: videos/file_86.mp4
          await bot.download_file(path, myFile)
          iS = message.video.file_size
          iW = message.video.width
          iH = message.video.height
          iL = message.video.duration
          Size = '● <b>file_size:</b>  <i>' + str(iS) + '</i>&#10;'
          Width = '● <b>width:</b> <i>' + str(iW) + '</i>&#10;'
          Height = '● <b>height:</b>  <i>' + str(iH) + '</i>&#10;'
          Duration = '● <b>duration:</b> <i>' + str(iL) + '</i>&#10;'
          FileID = '● <b>file_id:</b> <code>' + file_id + '</code>'
          iMsg = '✅ <u>Файл сохранен</u>:&#10;<code>' + myFile + '</code>&#10;' + Size + Width + Height + Duration + FileID
          await message.answer(iMsg, parse_mode=ParseMode.HTML)
#          file_info = await bot.get_file(video_id) # JSON данные по файлу
#          path = file_info.file_path # название файла вида: documents/file_25.docx
#          myFile = myDir + '/data/Video/' + iDay + '_' + str(path.strip('videos/')) # полный путь нового файла
#          await bot.download_file(path, myFile)
#          await message.answer("Файл добавлен в папку <b>../Video</b>: " + myFile, parse_mode=ParseMode.HTML)
          time.sleep(7) # пауза для красоты перед удалением "правого смс" на экране от пользователя
          await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
       except Exception as error: # Обработчик Ошибок Превышения размера файла!
          iMsg = 'ℹ️ <b>' + str(error) + '!</b>&#10;&#10;⛔ Файл превышает лимит в 20 Мбайт.&#10;💰 <b>Приобретайте коммерческую версию!</b>'
          await message.answer(iMsg, parse_mode=ParseMode.HTML)
          time.sleep(7) # пауза для красоты перед удалением "правого смс" на экране от пользователя
          await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True



@dp.message_handler(content_types=['audio'])
async def save_audio(message):
    if PASS and str(message.chat.id) in str(ID):
       try:
          file_id = message.audio.file_id # Получаем File ID, по кот. можем вызвать файл из облака очень быстро в этом Боте
          file_info = await bot.get_file(file_id) # JSON данные по файлу
          file_name = message.audio.file_name # Получаем "родное" имя файла *.mp4
          if file_name == None:
             file_name = file_info.file_path.strip('music/')
          myFile = myDir + '/data/Voice/' + str(file_name) # полный путь нового файла:
          path = file_info.file_path # название файла вида: music/file_86.mp4
          await bot.download_file(path, myFile)
          iS = message.audio.file_size
          iT = message.audio.title
          iP = message.audio.performer
          iL = message.audio.duration
          Size = '● <b>file_size:</b>  <i>' + str(iS) + '</i>&#10;'
          Title = '● <b>title:</b> <i>' + str(iT) + '</i>&#10;'
          Performer = '● <b>performer:</b>  <i>' + str(iP) + '</i>&#10;'
          Duration = '● <b>duration:</b> <i>' + str(iL) + '</i>&#10;'
          FileID = '● <b>file_id:</b> <code>' + file_id + '</code>'
          iMsg = '✅ <u>Файл сохранен</u>:&#10;<code>' + myFile + '</code>&#10;' + Size + Performer + Title + Duration + FileID
          await message.answer(iMsg, parse_mode=ParseMode.HTML)
#          file_info = await bot.get_file(audio_id)
#          path = file_info.file_path
#          myFile = myDir + '/data/Video/' + 'test.mp4'
#          await message.video[-1].download(myFile)
#          await message.reply("Фото добавлено: " + myFile)
          time.sleep(7) # пауза для красоты перед удалением "правого смс" на экране от пользователя
          await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
       except Exception as error: # Обработчик Ошибок Превышения размера файла!
          iMsg = 'ℹ️ <b>' + str(error) + '!</b>&#10;&#10;⛔ Файл превышает лимит в 20 Мбайт.&#10;💰 <b>Приобретайте коммерческую версию!</b>'
          await message.answer(iMsg, parse_mode=ParseMode.HTML)
          time.sleep(7) # пауза для красоты перед удалением "правого смс" на экране от пользователя
          await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True



@dp.message_handler(content_types=['sticker'])
async def save_sticker(message):
    if PASS and str(message.chat.id) in str(ID):
       try:
          file_id = message.sticker.file_id # Получаем File ID, по кот. можем вызвать файл из облака очень быстро в этом Боте
          file_info = await bot.get_file(file_id) # JSON данные по файлу
#          file_name = message.sticker.file_name # Нет такого поля !!!
#          if file_name == None:
          file_name = file_info.file_path.strip('stickers/file')
          iN = message.sticker.set_name
#          myFile = myDir + '/data/Stickers/' + str(file_name) # полный путь нового файла:
          myFile = myDir + '/data/Stickers/' + str(iN) + str(file_name) # полный путь нового файла:
          path = file_info.file_path # название файла вида: stickers/file_102.mp4
          await bot.download_file(path, myFile)
          iS = message.sticker.file_size
          iE = message.sticker.emoji
          iW = message.sticker.width
          iH = message.sticker.height
          Size = '● <b>file_size:</b>  <i>' + str(iS) + '</i>&#10;'
          Width = '● <b>file_size:</b>  <i>' + str(iW) + '</i>&#10;'
          Height = '● <b>file_size:</b>  <i>' + str(iH) + '</i>&#10;'
          Emoji = '● <b>file_size:</b>  <i>' + str(iE) + '</i>&#10;'
          Set_Name = '● <b>file_size:</b>  <i>' + str(iN) + '</i>&#10;'
          FileID = '● <b>file_id:</b> <code>' + file_id + '</code>'
          iMsg = '✅ <u>Файл сохранен</u>:&#10;<code>' + myFile + '</code>&#10;' + Size + Width + Height + Emoji + Set_Name + FileID
          await message.answer(iMsg, parse_mode=ParseMode.HTML)
          time.sleep(7) # пауза для красоты перед удалением "правого смс" на экране от пользователя
          await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
       except Exception as error: # Обработчик Ошибок Превышения размера файла!
          iMsg = '⛔️ <b>' + str(error) + '!</b>&#10;&#10;💰 <b>Приобретайте коммерческую версию!</b>'
          await message.answer(iMsg, parse_mode=ParseMode.HTML)
          time.sleep(7) # пауза для красоты перед удалением "правого смс" на экране от пользователя
          await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True



@dp.message_handler(content_types=['document'])
async def save_document(message):
    if PASS and str(message.chat.id) in str(ID):
       try:
          today = datetime.now(tz)
          iDay = today.strftime("%y-%m-%d")
          file_id = message.document.file_id # Получаем File ID, по кот. можем вызвать файл из облака очень быстро в этом Боте
          file_info = await bot.get_file(file_id) # JSON данные по файлу
          file_name = message.document.file_name # Получаем "родное" имя файла *.mp4
          if file_name == None:
             file_name = file_info.file_path.strip('documents/')
          myFile = myDir + '/data/PDF/' + str(file_name) # полный путь нового файла:
          path = file_info.file_path # название файла вида: documents/file_86.mp4
          iS = message.document.file_size
          Size = '● <b>file_size:</b>  <i>' + str(iS) + '</i>&#10;'
          FileID = '● <b>file_id:</b> <code>' + file_id + '</code>'
          await bot.download_file(path, myFile)
          iMsg = '✅ <u>Файл сохранен</u>:&#10;<code>' + myFile + '</code>&#10;' + Size + FileID
          await message.answer(iMsg, parse_mode=ParseMode.HTML)
#          document_id = message.document.file_id # Получаем File ID, по кот. можем вызвать файл из облака очень быстро в этом Боте
#          file_info = await bot.get_file(document_id) # JSON данные по файлу
#          path = file_info.file_path # название файла вида: documents/file_25.docx
#          ext = file_info.mime_type
#          myFile = myDir + '/data/PDF/' + iDay + '_' + str(path.strip('documents/')) # полный путь нового файла
#          await bot.download_file(path, myFile)
#          with open(myFile, 'w') as new_file: # 'wb' дает ошибку!!!
#             new_file.write(bot.download_file(file_info.file_path))
#          await message.answer("Файл добавлен в папку *../PDF*: " + myFile)
          time.sleep(7) # пауза для красоты перед удалением "правого смс" на экране от пользователя
          await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
       except Exception as error:
          iMsg = 'ℹ️ <b>' + str(error) + '!</b>&#10;&#10;⛔️ Файл превышает лимит в 20 Мбайт.&#10;💰 <b>Приобретайте коммерческую версию!</b>'
          await message.answer(iMsg, parse_mode=ParseMode.HTML)
          time.sleep(7) # пауза для красоты перед удалением "правого смс" на экране от пользователя
          await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
    else:
       return True



@dp.message_handler()
async def all_msg_handler(message: types.Message):
    if PASS and str(message.chat.id) in str(ID):
       btn_txt = message.text
       if btn_txt[0:5] == 'https':
          time.sleep(3) # пауза для красоты перед удалением "правого смс" на экране от пользователя
          await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку) или введенную команду
          reply_text = '☕️ ждем полной загрузки ⏳..'
          await message.answer(reply_text, parse_mode=ParseMode.MARKDOWN)
          subprocess.call(['/bin/bash', myDir + '/scripts/youtube_dl.sh', btn_txt])
#          subprocess.call(['cd', '/home/bunta/0.SSD/iKINO/izYoutube', ' && ', '/snap/bin/youtube-dl', btn_txt])
#          subprocess.call(['/bin/bash', './scripts/start_vlc.sh', btn_txt])
          reply_text = 'Ок! _Запускаю_ ...'
          await message.answer(reply_text, parse_mode=ParseMode.MARKDOWN)
       elif btn_txt[0:2] == '!!':
           subprocess.call(['/bin/bash', myDir + '/scripts/kill_proc.sh', 'sm'])
       elif btn_txt[0:1] == '!':
           subprocess.call(['/bin/bash', myDir + '/scripts/sms.sh', btn_txt.strip('!')])
#          reply_text = 'Сообщение на экране ПК: *[' + str(btn_txt) + ']*'
#          await message.answer(reply_text, parse_mode=ParseMode.MARKDOWN)
           msg = await message.answer('👏') # = хлопанье в ладоши
           await asyncio.sleep(3) # пауза независимая
           await msg.delete() # удаляет хлопанье в ладоши
       elif '%' in btn_txt:
          zVuk = btn_txt.strip('%')
          subprocess.call(['/bin/bash', myDir + '/scripts/volume.sh', zVuk])
          time.sleep(2) # пауза для красоты перед удалением "правого смс"
          await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку) или введенную команду
       elif btn_txt[0:2] == '?w':
          iMsg = '🔍 .. я спросил у <b>Яндекса</b>, ждите <b>секунд 10..</b>'
          sms = await bot.send_message(chat_id=message.chat.id, text=iMsg, parse_mode=ParseMode.HTML)
          await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку) или введенную команду
          subprocess.call(['/bin/bash', myDir + '/scripts/scrot_img.sh'])
#          time.sleep(8) # пауза для красоты перед удалением "правого смс"
          today = datetime.now(tz)
          iDay = today.strftime("%d-%m-%y_%H:%M")
          iMsg = '🌤 <i>Москва ' + str(iDay) + '</i>'
          with open(myDir + '/data/img00.png', 'rb') as img:
             await bot.send_photo(message.chat.id, img, iMsg, parse_mode=ParseMode.HTML)
          await bot.delete_message(chat_id=message.chat.id, message_id=sms.message_id) # Удаляем свое сообщение выше
       elif btn_txt[0:1] == '@':
          return True
       elif btn_txt[0:1] == '#':
          return True
       else:
          logger.debug('The answer is %r', btn_txt)  # print the text we've got
#          time.sleep(2) # пауза для красоты перед удалением "правого смс" на экране от пользователя
#          await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку) или введенную команду
          reply_text = '🗿'
          await message.answer(reply_text)
          time.sleep(3)
          reply_text = '⛔️ Ошибка ввода!'
          await message.answer(reply_text)
          time.sleep(2)
          await process_help_command(message)
#          await message.reply(reply_text, parse_mode=ParseMode.MARKDOWN)
#       await message.answer(reply_text, parse_mode=ParseMode.MARKDOWN)
    else:
       await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id) # Удаляем нажатую кнопку)
#       return True



#### Обработчик для чужаков (у кого не подходит ID, но подобрали стартовую команду!)
async def other_people(message):
    global PASS
    PASS = False
    cid = message.chat.id
    today = datetime.now(tz)
    Now = today.strftime("%d-%m_%H:%M")
#    Now = '28-05_14:46'
#    Now = today.strftime("%d.%m %H:%M:%S")
#    Now = time.strftime("%d-%m_%H:%M")
    Icon = '🚯'
    fName = '<b>First Name:</b> <code> ' + message.from_user.first_name + '</code>\n<b>Last Name:</b> '
#    lName = 'Last Name: <b>' + message.from_user.last_name + '</b>\n'
    lName = '<code> ' + message.from_user.last_name + '</code>'
    uName = '\n<b>User Name:</b> <code> ' + message.from_user.username + '</code>\n'
    Lang = '<b>Language Code:</b> <code> ' + message.from_user.language_code + '</code> 🇷🇺\n'
    Helo = '<b>Hello Mr.</b>' + lName + '!\n<code>++++++++++++++++++++++++</code>\n'
    iMsg = Helo + '<b>Now:</b><i> ' + Now + '</i>\n' + fName + lName + uName + Lang + '<b>ID:</b> [<code> ' + str(cid) + ' </code>]©️'
#    await message.reply('*Hello World!* %s' % em00 + , parse_mode=ParseMode.MARKDOWN, reply_markup=types.ReplyKeyboardRemove())
    my_log = '<b>vtica:</b> <code>' + str(cid) + '</code> ' + Icon + ' <b>' + uName + '</b> ' + Now + ' ⚙️ ' + message.text
    await bot.send_message(ID[1], my_log, parse_mode=ParseMode.HTML)  # Отправляем Log на Второй моб
    await message.reply(iMsg, parse_mode=ParseMode.HTML, reply_markup=types.ReplyKeyboardRemove()) # Выдаем инфо на Экран пишушего!
    time.sleep(1) # пауза для красоты перед удалением "правого смс" на экране от пользователя
    await bot.delete_message(chat_id=cid, message_id=message.message_id) # Удаляем нажатую кнопку)
# Временная отправка инфо + ID на основной моб для Корректировки zInfo.0
    await bot.send_message(ID[0], iMsg, parse_mode=ParseMode.HTML) # ВРЕМЕННО!



if __name__ == "__main__":  # проверяет, был ли файл запущен напрямую, а не импортирован
# При импорте, переменная будет содержать имя модуля, из которого произошел импорт.
    while True:
        try:                # добавляем try для бесперебойной работы
            executor.start_polling(dp, on_startup=on_startup, skip_updates=True) # Запуск бота
        except Exception as error:
            iMsg = '⛑ <b>' + str(error) + '!</b>&#10;💰 <b>Приобретайте коммерческую версию!</b>&#10;🚬 ..перекур 5 сек.'
            print (iMsg)
#            await message.answer(iMsg, parse_mode=ParseMode.HTML)
            time.sleep(5)   # перекур 5 сек!
#        except:             # в случае падения
#            time.sleep(5)   # перекур 5 сек!
