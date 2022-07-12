#! /bin/bash

read -p "Connection to Google Drive ? (Y/n) : " is_drive

apt -y update
apt -y upgrade
apt install python3 -y
apt install python3-pip -y
pip3 install GPUtil
pip3 install requests
mkdir /home/user/script
cd /home/user/script
wget https://raw.githubusercontent.com/frogizz31/mining/main/test.py
wget https://github.com/prasmussen/gdrive/releases/download/2.1.1/gdrive_2.1.1_linux_386.tar.gz
tar -xvf gdrive_2.1.1_linux_386.tar.gz
if [ "$is_drive" = "Y" ]; then 
  ./gdrive about
fi
python3 test.py
echo '0 * * * * python3 /home/user/script/test.py' >> /hive/etc/crontab.root

read -p "Reboot to apply changes ? (Y/n) : " is_reboot

if [ "$is_reboot" = "Y" ]; then 
  reboot
fi
