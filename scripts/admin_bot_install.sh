#!/bin/bash
# 26-05-2021 [ver.1.0] Script to Install Telegram & Download admin_linux.py from Web0 to Test
b=$(tput bold)
c0="\E[0;39m"   # c_std

myINFO="/etc/ssh/zInfo.0"
iHome=$(cat $myINFO | grep -v "#" | grep Home= | cut -d"=" -f2)
iUser=$(cat $myINFO | grep -v "#" | grep User= | cut -d"=" -f2)

xPort="2299"                           # Remote Web0 Port
xWeb="pi@81.90.3.17"                   # Remote Web0 IP
xDir="/home/pi/ARCHIVE/MyKeys.000/000" # Common Folder with Configs on Web0

iDir="$iHome/.ssh"                     # Local Dir for SSH-Keys & Private Configs
iKey="$iDir/id_ed25519.web0"           # Local Web0 Key in home Folder ~/.ssh
iStr="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"

# [0] Install Python3, Pip3 & TeleBot [PyTelegramBotAPI]!!
python3 -V || sudo apt install python3 -y
pip3 -V || sudo apt install python3-pip -y
pip3 install --upgrade pip
pip3 show pytelegrambotapi || pip3 install -U pytelegrambotapi

aWord="alias python='python3'"
aFile="$iHome/.bash_aliases"
aAlias=$(cat $aFile | grep "$aWord") # Test alias python='python3'
if [ "aAlias" == "" ]; then
 echo "$aWord" >> $aFile             # Add alias
 . $iHome/.bashrc                    # Activate alias
fi

# [1] Check & Get Python Config File
jFile="myconfig.py"                   # Common Private Config File on Web0 for Python3 Progs
if ! [ -f "$iDir/$jFile" ]; then
 scp -P $xPort -i $iKey $iStr $xWeb:$xDir/$jFile $iDir/  # Get myconfig.py [Web0] -> [~/.ssh]
 chmod 600 $iDir/$jFile
fi

# [2] Check & Get Admin_Linux.py Prog
zDir="$iHome/scr/fig/1.Telegram"
zFile="admin_linux.py"
if ! [ -f "$zDir/$zFile" ]; then
 if ! [ -d "$zDir" ]; then mkdir -p $jDir; fi
 scp -P $xPort -i $iKey $iStr $xWeb:$xDir/$zFile $zDir/  # Get admin_linux.py [Web0] -> [~/.ssh]
 chmod 755 $zDir/$zFile
fi

my_link="$zDir/$jFile"
if ! [ -L ${my_link} ] && ! [ -e ${my_link} ]; then
 ln -s $iDir/$jFile $zDir/
fi

echo -e ${b}"\npython $zDir/$zFile"${c0}
echo ""
