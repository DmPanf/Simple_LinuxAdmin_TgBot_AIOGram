#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 28-05-2021
#

#from aiogram.dispatcher import Dispatcher
#from aiogram.types import ParseMode
#from aiogram.utils.markdown import text, bold, italic, code, underline, strikethrough
from aiogram.utils.markdown import text
from aiogram import types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

em00 = "♻️"
#startMsg = "*%s*, Привет!\n♻️  Выбираем задачу:" # Стартовое приглашение после ввода Кодового Слова
startMsg = " <b>%s</b>, Привет! 🖐" # Стартовое приглашение после ввода Кодового Слова
#foto1 = 'AgADAgADfqkxG2r6mEuUhFtqBaBgwdrdtw4ABKnYUDKtE82vcSkCAAEC' # tiger


# [0] ------ MAIN MENU -------]

but01 = KeyboardButton('💻 SysINFO')
but02 = KeyboardButton('⌨️  PC Control')
but03 = KeyboardButton('📤 SendFile')
#but04 = KeyboardButton('💡HELP &Tips📍')
but04 = KeyboardButton('💡 HELP')
but05 = KeyboardButton('📍 TIPs')

but11 = KeyboardButton('SMART 🏠')
but12 = KeyboardButton('💾 SOFT')
but13 = KeyboardButton('📽  KINO')
but14 = KeyboardButton('📺 DLNA')

# default row_width is 4, so here we can omit it actually
kb_main_menu = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True, one_time_keyboard=True)
#       but1_txt = ('💻System ℹ', '⚙️ PC Control', '📤 Send Files', '💡HELP &Tips📍')
#       kb_markup.row(*(types.KeyboardButton(text) for text in but1_txt))
#       but2_txt = ('🏠Smart House 🛁', '💾 Programs', '📽 KINO📺')
#       kb_markup.add(*(types.KeyboardButton(text) for text in but2_txt))
#kb_main_menu.add(but01, but02, but03, but04)
#kb_main_menu.add(but11, but12, but13, but14)
kb_main_menu.add(but01, but02, but03)
kb_main_menu.add(but12, but13, but14)
kb_main_menu.add(but11, but05, but04)


# ------ BACK -------]
but20 = KeyboardButton('⬅️️ BACK')
but30 = KeyboardButton('⬅️')


# [1] ------ SysInfo ------------]
help_sysinfo = text(
'💻SysInfo',
'\nИз списка скриптов в папке *sysinfo* отображаются названия скриптов',
'для сбора информации и сохранения в файлах с теми же названиями, но расширением .txt'
)


# [2] ------- PC Control -------]
help_pc_control = text(
'*🔴 StopPC*', '= выключить ПК\n',
'*🔄 Reboot*', '= перезагрузка\n',
'*☢️️  Config*', '= настройки ПК\n',
'*📡️️ Proxy*', '= openVPN 💵\n',
'*🌐 VPN*', '= разрешение на администрирование (*openSSH*)\n',
'*💎 t.me*', '= доступ к Linux через Telegram\n',
'*🈴 VNC*', '= аналог RDP-доступа к ПК 💵'
)

but21 = KeyboardButton('🔴StopPC')
but22 = KeyboardButton('🔄Reboot')
but23 = KeyboardButton('☢️️ Config')

#but01 = KeyboardButton('') = ('💻SysInfo')
#but12 = KeyboardButton('💾 Soft')
but25 = KeyboardButton('🕸 web') # Trigger = доступ к папке и файлам через Web 80 порт на python3
but26 = KeyboardButton('🌐VPN') # Открыть порт для доступа к ПК [выключение по таймеру мин через 10-20]
but27 = KeyboardButton('💎t.me') # Запуск admin_linux.py [выключение по таймеру мин через 10-20]
but28 = KeyboardButton('🈴VNC') # Доступ к рабочему столу = Trigger
but29 = KeyboardButton('📡proxy') # OpenVPN Trigger

kb_pc_menu = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True, one_time_keyboard=True)
kb_pc_menu.add(but20, but21, but22, but23)
kb_pc_menu.add(but29, but26, but27, but28)


# [3] ------- Send Files -------]
help_send_files = text(
'📤 Папки с файлами:&#10;'
'📷', '= Фото', '📹', '= Видео&#10;',
'🎧', '= mp3', '📂', '= PDF&#10;',
'♦️♠️', '= MediaGroup®️&#10;&#10;',
'🕸  <b>web</b>', '= быстрый запуск <b>Web-сервера</b> на Python3&#10;',
'🗄 mem', '= шпаргалка - рабочие скриншоты️&#10;&#10;',
'ℹ️ Отправить файл <b>Боту</b> на ПК можно в любой момент&#10;',
'🔱 Ссылки из <b>Youtube</b> запускают видео сразу в полный рост&#10;<b>Пример:</b>&#10;[<code>https://youtu.be/xDsnYzGyxe0</code>]©️',
)

but31 = KeyboardButton('📷photo') # jpg & png
but33 = KeyboardButton('📹video') # mov & mp4
but32 = KeyboardButton('🎧audio') # mp3
but34 = KeyboardButton('📂') # PDF & DOCs Files
but35 = KeyboardButton('♦️♠️') # MediaGroup
#but36 = KeyboardButton('🔮') # VideoNote

but48 = KeyboardButton('🗄 mem')  # Рабочие шпаргалки в виде img

kb_send_menu = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
kb_send_menu.add(but30, but25, but48, but35)
kb_send_menu.add(but31, but33, but32, but34)


# [4] ------- HELP & TIPs -------]
but41 = KeyboardButton('🐧linux')  # Шпаргалка по командам Linux
but42 = KeyboardButton('💎/t.me')  # Форматирование в Telegram
but43 = KeyboardButton('📺info')  # Описание формата DLNA
but44 = KeyboardButton('👮jobs')  # Сcылки на рабочие аккаунты и Группы/Каналы
but45 = KeyboardButton('🗞news')  # Рекомендации по новостям
but46 = KeyboardButton('📎link') # Ссылки на сайты (внутри Телеграм)
but47 = KeyboardButton('🛠tools')  # Интсрументы = полезные Боты

kb_help_menu = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True, one_time_keyboard=True)
kb_help_menu.add(but20, but41, but42, but45)
#kb_help_menu.add(but45, but44, but48, but46, but47)
kb_help_menu.add(but46, but44, but48, but47)


help_message = text(
'🔘 Меню может скрываться в трей 🎛\n',
'/help24', '= краткая справка\n',
'*/off/stop/by*', '= убрать меню\n\n',
'💻 *Sys Info*', '= о системе\n',
'⌨️  *PC Control*', '= VPN/Web; PC-admin/вкл/выкл\n',
'📤  *Send Files*', '= отправка в Telegram файлов из папок ПК\n\n',
'💾  *SOFT*', '= запуск программ\n',
'📽  *KINO*', '= запуск видео\n',
'📺 *DLNA*', '= кино по сети\n\n',
'*SMART* 🏠', '= в разработке (w8)\n',
'📍 *TIPs*', '= дополнительные функции\n',
'💡 *HELP*', '= полезная информация\n'
)

help_command = text(
'🔘 Для перезапуска набрать&#10;',
'<b>/кодовое слово</b> ', '= [/start]&#10;&#10;',
'<b>[!]</b>', '= вывод сообщений (команд) на экране ПК&#10;',
'<b>[!!]</b>', '= сброс сообщений&#10;',
'<b>[!🕰  =!t][!☎️  =!m][!☀️  =!w][!ℹ️ =!i]</b>[<code>!lsusb</code>]',
'[<code>!ls</code>][<code>!hostname -I</code>][<code>!lsblk</code>][<code>!hostnamectl</code>]&#10;&#10;',
'<b>[%85][34%]</b>', '= Sound Volume&#10;&#10;',
'<b>[<a href="https://telegram.org/">встроенная ссылка</a>]</b> ®️&#10;',
'[<code>автокопирование на смартфоне</code>] ©️&#10;',
'<b>[?w]</b>', '🌤 Яндекс Погода☔️&#10;',
'[@]', ' 🔸 Task ToDo (w8)&#10;',
'[#]', ' 🔸 MyNotes (w8)&#10;'
)


about_tme = text(
'💡 Форматирование <b>t.me</b>:&#10;',
'- <b>CTRL/CMD + B/I</b> жирный шрифт/курсив&#10;',
'- <b>CTRL/CMD + SHIFT + M</b> моноширинный шрифт&#10;',
'- <b>CTRL/CMD + K</b> добавить или отредактировать гиперссылку&#10;',
'- <b>CTRL/CMD + SHIFT + N</b> убрать форматирование&#10;',
'++++++++++++++++++&#10;',
'1. [<i>наклон</i>] = по два подчеркивания [__]&#10;',
'2. [<b>жирный текст</b>] = по две звездочки [**]&#10;',
'3. [<code>моноширинный</code>] = по одной обратной кавычке [`]&#10;',
'4. [<a href="https://t.me/zaq_ki_no1_bot">ссылка</a>] = [Текст](https://t.me/Xbot)&#10;'
)


about_dlna = text(
'📺 *DLNA* (*Digital Living Network Alliance* - Альянс живущей цифровой сети) - это некий набор стандартов,',
' которые дают возможность по беспроводной (*Wi-Fi*) и проводной (*Ethernet*) сети всем совместимым устройствам',
' *(ноутбук, планшет, мобильный телефон, игровая приставка, принтер, видеокамера...)* передавать и принимать',
'для воспроизведения фотографии, видео и аудио файлы.\n\n',
'✅ Все именитые бренды такие как *Microsoft, Intel, Hewlett-Packard, Nokia, Samsung, LG, Sony...* состоят в этом цифровом альянсе!\n\n',
'🍎 *Apple* совместно с компанией *BridgeCo* разработала свой стандарт (технология и протокол) *AirPlay*,',
' который поддерживают устройства от таких производителей, как *Bowers & Wilkins, iHome, Marantz, JBL.*\n\n',
'🖥 *Server*', '= папки с удаленного Сервера автоматически попадают в пул доступного медиа-контента в ЛВС!'
)


about_jobs = text(
'®️️️ *Рабочие Чаты и Каналы:*\n',
'🔹[ВТИ vs Covid19](https://t.me/c/1474952417/142)\n',
'🔹[Новости энергетики vti](https://t.me/oaovti)\n',
'🔹[ВТИ](https://t.me/c/1359583988/496) ',
'🔹[СПРАВКА](https://t.me/c/1495412438/86)\n'
'🔻[Битва за ВТИ...](https://t.me/joinchat/D00OpnU-lg756WQm)\n',
'🔻[Финансы ВТИ](https://t.me/joinchat/FTixqAc9PK5UaexO)\n',
'🔻[Кадры ВТИ](https://t.me/joinchat/GM2ca-JXGyyZR4FF)',
'🔻[DNP](https://t.me/dnp_gtt)\n\n',
'🔻[Монологи по пути домой](https://t.me/rafftips)\n',
'🌐 [Интер РАО](https://t.me/iraogeneration)\n',
'🌐 [Государство в Telegram](https://t.me/GovInfo/378)\n\n',
'💎 [Свой Бот с BotFather](https://t.me/BotFather)\n',
'🧠 [Помощник опросов](https://t.me/vote)\n',
'♻️ [Admin Linux Bot](https://t.me/zaq_ki_no1_bot)\n\n',
)


about_news = text(
'®️️️ *Новостные ленты:*\n',
'🔖 [Президент России](https://t.me/kremlininfo)\n',
'🔖 [Технологии будущего](https://t.me/tech_ru)\n',
'🔖 [Главные Новости РИА](https://t.me/rian_ru)\n',
'🔖 [ПРАЙМ](https://t.me/prime1)\n',
'🔖 [Оперштаб Москвы](https://t.me/COVID2019_official)\n',
'🔖 [Московские новости](https://t.me/themoscowdailynews)\n',
'🔖 [Новости Москва 2021](https://t.me/Moscow_00)\n',
'🔖 [Воробьёв LIVE](https://t.me/vorobiev_live)\n',
'🔖 [Energy Today](https://t.me/energytodaygroup)\n',
'🔖 [Нефть и Капитал](https://t.me/oil_capital)\n',
'🔖 [ЭНЕРГОПОЛЕ](https://t.me/energopolee)\n',
'🔖 [Операционная](https://t.me/Operation_med)\n',
)


about_links = text(
'®️️ *Интернет-ресурсы:*\n',
'🌐 [Сайт ОАО "ВТИ"](http://vti.ru/)\n',
'🌐 [Сайт ПАО "Интер РАО"](https://www.interrao.ru/)\n',
'🌐 [Фонд ЭБГ](https://energy-fund.ru/)\n',
'🌐 [Сайт Сергея Собянина](https://www.sobyanin.ru)\n',
'🌐 [COVID Live Update](https://www.worldometers.info/coronavirus/#countries)\n',
'🌐 [МинЗдрав](https://minzdrav.gov.ru)\n',
'🌐 [Коронавирус COVID–19](https://стопкоронавирус.рф/)\n'
)


about_others = text(
'®️️ *Инструменты:*\n',
'📩 [Почта GMail](https://t.me/GmailBot)\n',
'🚌 [Яндекс Карты](https://t.me/YandexMapsBot)\n',
'🔍 [Яндекс поиск по картинкам](https://t.me/pic)\n',
'🖍 [Редактор изображений](https://t.me/Photo_editor_bot)\n',
'🍔 [Яндекс Еда](https://t.me/yandex_eda_bot)\n',
'🎧 [Яндекс Музыка](https://t.me/music_yandex_bot)\n',
'🎼 [Музыка Deezer](https://t.me/DeezerMusicBot)\n',
'🏝  [Лучшие фотографии со всего мира](https://t.me/NationalGeographic)\n',
'🧮 [Обработка фото с помощью нейросетей](https://t.me/DeepPicBot)\n',
'🔖 [Wiki On-line](https://t.me/wiki)\n'
)


# [5] ------- SMART HOUSE -------]
help_smart_house = text(
'⚡(️w8) = *Меню в разработке* ⚡️',
'\n.. для автоматизации процессов, сбора и обработки информации, управления технологиями или устройствами',
'*IoT:*\n', '🌡', '🚽🚰🛁', '🔌', '💡', '🔐',
'\n\n🌡📈', '= График *температуры ЦПУ*\n',
'...'
)


but50 = KeyboardButton('🌡📈')
but51 = KeyboardButton('🚰🛁')
but52 = KeyboardButton('🔌')
but53 = KeyboardButton('💡')
but54 = KeyboardButton('🔐')
but55 = KeyboardButton('🏠окна')
but56 = KeyboardButton('🚪двери')
but57 = KeyboardButton('⚡️реле')
#but58 = KeyboardButton('🛣 игры')
but58 = KeyboardButton('🎮') # Игры и развлечения
but91 = KeyboardButton('☎️ Контакт', request_contact=True) # Отправка происходит атоматически без обработчика
but92 = KeyboardButton('🆔Телеграм')
but93 = KeyboardButton('🌍Локация', request_location=True) # Отправка происходит атоматически без обработчика
but94 = KeyboardButton('💊') # Аптечка в дорогу
#but95 = KeyboardButton('🌦погода')
but95 = KeyboardButton('🌤☔️')
#but96 = KeyboardButton('📸ipCam') # Отправка фото с IP-Cam
but96 = KeyboardButton('📸') # Отправка фото с IP-Cam
but97 = KeyboardButton('🤖робот')

kb_smart_menu = types.ReplyKeyboardMarkup(row_width=8, resize_keyboard=True)
kb_smart_menu.add(but30, but50, but51, but52, but53, but54)
kb_smart_menu.add(but55, but56, but57, but97)
#kb_smart_menu.add(but91, but92, but93)
#kb_smart_menu.add(but94, but95, but96, but58)


tips_message = text(
'Дополнительные инструменты:\n',
'💊', '= *аптечка* в дорогу\n',
'🌦 ', '= *Прогноз погоды*\n',
'📸', '= *Фото* c IP-Cam\n',
'🎮', '= J4F & Relax\n\n',
'☎️ ', '= Отправка контакта\n',
'🆔', '= Telegram ID\n',
'🌍', '= Отправка геопозиции'
)

kb_tips_menu = types.ReplyKeyboardMarkup(row_width=5, resize_keyboard=True)
kb_tips_menu.add(but30, but94, but95, but96, but58)
kb_tips_menu.add(but91, but92, but93)


##but61 = KeyboardButton('⬅️️ BACK')
#but62 = KeyboardButton('⬆️')
#but63 = KeyboardButton('🔂Reload')
#but64 = KeyboardButton('⬅️️')
#but61 = KeyboardButton('🈁')
#but65 = KeyboardButton('➡️')
#but66 = KeyboardButton('ℹ️NFO')
#but67 = KeyboardButton('⬇️')
#but68 = KeyboardButton('📸.img')

#kb_robot_menu = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
#kb_robot_menu.add(but20, but62, but63)
#kb_robot_menu.add(but64, but61, but65)
#kb_robot_menu.add(but66, but67, but68)

# [6] ------- SOFT -------]
help_soft = text(
'💡 _Краткое описание:_\n',
'🔸*conky*', '= виджет - системный монитор системы\n',
'🔸*gnome-disks*', '= простое управление дисками\n',
'🔸*gnome-software*', '= Центр Приложений\n',
'🔸*mate-calc*', '= калькулятор (4 режима работы)\n',
'🔸*remmina*', '= удобный клиент удаленного рабочего стола (RDP)\n',
'🔸*telegram-desktop*', '= бесплатное SuperApp\n',
'🔸*thunar*', '= файловый менеджер для XFCE\n',
'🔸*vlc*', '= бесплатный и свободный медиаплеер\n',
'🔸*xfce4-terminal*', '= лёгкий и простой эмулятор терминала для X11\n'
)

# [7] ------- KINO -------]
# Common InlineKeyboard
#btn_kino_kb = types.InlineKeyboardMarkup(row_width=3)
#text_and_data = (
#   ('📁 MAIN', '#D1'),
#   ('⏹ STOP [VLC]', '#Svlc'),
#   ('📁 izYoutube', '#D2'),
#)
#row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
#btn_kino_kb.row(*row_btns)


# [8] ------- DLNA -------]
help_dlna = text(
'🔎 *dlna* = набор стандартов для удобного просмотра медиаконтента в домашней сети:',
'*ТВ, планшеты, смартфоны, ПК, медиа-плейеры, ...*\n\n',
'🆗 *Status*', '= Информация по DLNA и Серверам\n',
'🔠 *D.Base*', '= Обновить базу Кино (*force-reload*) после добавления новых файлов\n',
'🖥 *Server*', '= Подключить удаленный Сервер *Кино+*\n',
'🔄 *Reload*', '= Перезапустить сервисы DLNA\n',
'🆙️ *Start*', '= Запустить DLNA\n',
'⏹  *STOP*', '= Остановить все процессы!\n'
)

but81 = KeyboardButton('🆗 Status')
but82 = KeyboardButton('🔠 D.Base')
but83 = KeyboardButton('🖥 Server')
but85 = KeyboardButton('🔄 Reload')
but84 = KeyboardButton('🆙 Start')
but86 = KeyboardButton('⏹  STOP')

kb_dlna_menu = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
kb_dlna_menu.add(but20, but81, but82, but83)
kb_dlna_menu.add(but86, but85, but84, but43)

logo = """
<code>.-..-..-..---.  .--. </code>
<code>: :: `: :: .--': ,. :</code>
<code>: :: .` :: `;  : :: :</code>
<code>: :: :. :: :   : :; :</code>
<code>:_;:_;:_;:_;   `.__.'</code>
"""
