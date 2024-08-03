#!/bin/bash
# 29-05-2021
# Продвинутый запуск основного Telegram Bot на Сервер
# [CRON]
# [Telegram]
# -d parse_mode=markdown   Отправка форматированного текста

export DISPLAY=:0
export SHELL=/bin/bash
export HOME=/home/bunta
export USER=bunta
export LOGNAME=bunta
export TERM=xterm-256color
export PATH=/home/bunta/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
export XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
export PWD=/home/bunta
export LANGUAGE=ru:en
export LANG=ru_RU.UTF-8
export SHLVL=1
export XDG_RUNTIME_DIR=/run/user/1000
export LC_TIME=ru_RU.UTF-8
export XDG_SESSION_CLASS=user
export LC_IDENTIFICATION=ru_RU.UTF-8

myINFO="/etc/ssh/zInfo.0"
#iDir=$(cat $myINFO | grep -v "#" | grep Home= | cut -d"=" -f2)
TOKEN1=$(/usr/bin/cat $myINFO | /usr/bin/grep -v "#" | /usr/bin/grep TOKEN11= | /usr/bin/cut -d"=" -f2)
CHAT_ID1=$(/usr/bin/cat $myINFO | /usr/bin/grep -v "#" | /usr/bin/grep CHAT_ID1= | /usr/bin/cut -d"=" -f2)
CHAT_ID2=$(/usr/bin/cat $myINFO | /usr/bin/grep -v "#" | /usr/bin/grep CHAT_ID2= | /usr/bin/cut -d"=" -f2)
CHAT_ID3=$(/usr/bin/cat $myINFO | /usr/bin/grep -v "#" | /usr/bin/grep CHAT_ID3= | /usr/bin/cut -d"=" -f2)
myName=$(/usr/bin/cat $myINFO | /usr/bin/grep -v "#" | /usr/bin/grep Name= | /usr/bin/cut -d"=" -f2)

URL1="https://api.telegram.org/bot$TOKEN1/sendPhoto"
URL2="https://api.telegram.org/bot$TOKEN1/sendMessage"
File="/home/bunta/scr/AIOGram/data/00.jpg"

iTest=$(/usr/bin/ps -fC python3 | /usr/bin/grep 'main.py')
if [ "$iTest" == "" ]; then
#/usr/bin/screen -dmS MainBot /usr/bin/python3 /home/bunta/scr/AIOGram/main.py # ПОКА НЕ ВОЙДЕШЬ В [screen -r] НЕ РАБОТАЕТ ВСЕ У [inxi -i]
# 💊 стоит убрать из строки запуска screen ключик -d (deattach), то все работает ‼️
/usr/bin/screen -d -m -S MainBot /usr/bin/python3 /home/bunta/scr/AIOGram/main.py # -d = PROBLEM! = лучше добавить [&]
#/usr/bin/python3 /home/bunta/scr/AIOGram/main.py & # ПРОБЛЕМ С ЗАПУСКОМ [inxi] ЕЩЕ БОЛЬШЕ!!!
##  iPid=$(/usr/bin/ps -fC python3 | /usr/bin/grep main.py | /usr/bin/awk {'print $2'})
##  Msg=$(/usr/bin/echo -e "⚙️ *VTI* Comp Assistant 💡 *[$iPid]*\n...в ожидании команд...")
##  Msg=$(/usr/bin/echo -e "⚙️ *VTI* Comp Assistant 💡\n*[$iPid] кодовое слово?*")
## заменить на vvm [3] $CHAT_ID3 -> /etc/ssh/zInfo.0

## Работающая ТЕМА:
#  Msg=$(/usr/bin/echo -e "⚙️ *VTI* Comp Assistant: 💡\n*- Жду кодовое слово...*")
#  /usr/bin/curl -s -X POST $URL1 -F chat_id=$CHAT_ID3 -F photo="@$File" -F caption="$Msg" -F parse_mode=markdown
#  /usr/bin/curl -s -X POST $URL1 -F chat_id=$CHAT_ID1 -F photo="@$File" -F caption="$Msg" -F parse_mode=markdown

##  /usr/bin/curl -s -X POST $URL2 -d chat_id=$CHAT_ID3 -d parse_mode=markdown -d text="$Msg" # заменить на vvm [3] $CHAT_ID3
##  /usr/bin/curl -s -X POST $URL2 -d chat_id=$CHAT_ID1 -d parse_mode=markdown -d text="$Msg"
fi

exit 0
