# Pybuster v1.0
Pybuster is a powerful multithreaded web directory fuzzer written in python. it uses pypy to run which makes it even faster.  
It can find valid pages by looking at the word or charecter length, this is really useful in situations when wildcard response is enabled.

## Prerequisites
pybuster uses pypy so it must be installed before using the tool  
```
apt install pypy
```
## Installing
```
git clone https://github.com/r4j1337/pybuster
cd pybuster/
./install.sh

root@kali:~/pybuster# pybuster -h
usage: pybuster [-h] [-w WORDLIST] [-u URL] [-t THREADS] [--auto] [-f]
                [-a USER_AGENT] [-c COOKIES] [-fs] [-e] [-p PROXY] [-q]
                [-o OUTPUT] [-s STATUS_CODES] [-U USERNAME] [-P PASSWORD]
                [-x EXTENSIONS]
```

![Screenshot](https://raw.githubusercontent.com/r4j1337/pybuster/master/images/help.png)  
![Screenshot](https://raw.githubusercontent.com/r4j1337/pybuster/master/images/example.png)    
![Screenshot](https://raw.githubusercontent.com/r4j1337/pybuster/master/images/wlen.png)
