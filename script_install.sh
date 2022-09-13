#! /bin/bash

apt -y update
apt -y upgrade
apt install python3 -y
apt install python3-pip -y
pip3 install GPUtil
pip3 install requests
python3 -m pip install -U discord.py
mkdir /home/user/script
cd /home/user/script
wget https://raw.githubusercontent.com/frogizz31/mining/main/test.py
python3 test.py
echo '0 * * * * python3 /home/user/script/test.py' >> /hive/etc/crontab.root

read -p "Reboot now to apply changes ? (Y/n) : " is_reboot

if [ "$is_reboot" = "Y" ]; then 
  reboot
fi
