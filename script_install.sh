#! /bin/bash

apt -y update &&
apt -y upgrade &&
apt install python3 -y &&
pip3 install GPUtil &&
pip3 install requests &&
mkdir /home/user/script &&
cd /home/user/script &&
wget https://github.com/prasmussen/gdrive/releases/download/2.1.1/gdrive_2.1.1_linux_386.tar.gz &&
tar -xvf gdrive_2.1.1_linux_386.tar.gz &&
./gdrive about &&
./gdrive download test.py &&
python3 test.py
