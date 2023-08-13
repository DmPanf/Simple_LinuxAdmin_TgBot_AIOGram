#!/bin/bash
# 29-05-2021
# Скрипт для осианова всех запущенных скриптов на Python3

#list=$(ps -fC python3 | grep "$HOME" | awk {'print $2'})
#for word in $myPy; do
for word in {'pts/','SCREEN','main.py','admin_linux.py'}; do
  echo $word
  list=$(ps -fC 'python3' | grep "$word" | awk {'print $2'})
  for iPy in $list; do
   echo $iPy
    kill -9 $iPy
  done
done
echo -e "$list\n Ok!"

exit 0
