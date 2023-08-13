# admin_linux.py

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 04-05-2021 Bot to Get acsses into Server & Start Linux Commands for Admins
#                                           # Бот позволяет получить доп.доступ к ПК = ОПАСНО!!!
from subprocess import check_output
import telebot
from telebot import types                   # Добавляем импорт кнопок
import os, sys, time

#hDir = os.getenv("HOME")
#sys.path.append(f"{hDir}/.ssh/")
from myconfig import *
#reload(sys)
#sys.setdefaultencoding('utf8')
user_id = USER_ID_01
TOKEN = TOKEN_01
#user_id = USER_ID_11 # VVM Main ID

bot = telebot.TeleBot(TOKEN)

#TOKEN = '1420657354:AAHXXa3cX_cuZjGzQkuCHKlymoalX10ftIE' # [ZAQ Proba Serv] = vti-monitor
#user_id = 408372130                         # id main [gtt]

@bot.message_handler(content_types=["text"])
def main(message):
    cid = message.chat.id
    if str(cid) in str(ID):
#   if (user_id == message.chat.id):         # проверяем, что пишет именно владелец
      comand = message.text                 # текст сообщения
      markup = types.InlineKeyboardMarkup() # создаем клавиатуру
      button = types.InlineKeyboardButton(text="Повторить ["+comand+"]", callback_data=comand) # создаем кнопку
      markup.add(button)                    # добавляем кнопку в клавиатуру
      try:                                  # если команда невыполняемая - check_output выдаст exception
#         bot.send_message(message.chat.id, check_output(comand, shell = True))
                                            # вызываем команду и отправляем сообщение с результатом
         bot.send_message(user_id, check_output(comand, shell = True), reply_markup = markup)
      except:
         bot.send_message(user_id, "Invalid input")   # если команда некорректна

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
  comand = call.data                        # считываем команду из поля кнопки data
  try:                                      # если команда не выполняемая - check_output выдаст exception
     markup = types.InlineKeyboardMarkup()  # создаем клавиатуру
     button = types.InlineKeyboardButton(text="Повторить ["+comand+"]", callback_data=comand)                   # создаем кнопку и в data передаём команду
     markup.add(button)                     # добавляем кнопку в клавиатуру
     bot.send_message(user_id, check_output(comand, shell = True), reply_markup = markup)  # вызываем команду и отправляем сообщение с результатом
  except:
     bot.send_message(userid, "Invalid input") # если команда некорректна

if __name__ == '__main__':
    while True:
        try:                                # добавляем try для бесперебойной работы
            bot.polling(none_stop=True)     # запуск бота
        except:
            time.sleep(10)                  # в случае падения
