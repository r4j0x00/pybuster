#!/bin/bash
check=$(which pypy)
if [ $? -ne 0 ]
then
	apt install pypy -y
fi
wget https://bootstrap.pypa.io/get-pip.py -qO- | pypy
pypy -m pip install -r requirements.txt
sudo cp pybuster.py /usr/bin/pybuster
sudo chmod 755 /usr/bin/pybuster
echo "[+] Installed pybuster"
