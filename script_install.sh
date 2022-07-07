#! /bin/bash

apt -y update
apt -y upgrade
apt install python3 -y
apt install python3-pip -y
pip3 install GPUtil
pip3 install requests
mkdir /home/user/script
cd /home/user/script
wget https://github.com/frogizz31/mining/releases/download/v1.0/test.py
wget https://github.com/prasmussen/gdrive/releases/download/2.1.1/gdrive_2.1.1_linux_386.tar.gz
tar -xvf gdrive_2.1.1_linux_386.tar.gz
./gdrive about
python3 test.py
echo '0 * * * * python3 /home/user/script/test.py' >> /hive/etc/crontab.root
