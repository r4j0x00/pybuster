#!/bin/bash
apt install pypy -y
wget https://bootstrap.pypa.io/get-pip.py
pypy get-pip.py
pypy -m pip install requests
pypy -m pip install argparse
sudo cp pybuster.py /usr/bin/pybuster
sudo chmod 755 /usr/bin/pybuster
rm get-pip.py
echo "[+] Installed pybuster"
