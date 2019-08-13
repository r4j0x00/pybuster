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

## Built-in help menu
```
root@kali:~/test/pybuster# pybuster -h
usage: pybuster [-h] [-w WORDLIST] [-u URL] [-t THREADS] [-wf] [-f]
                [-a USER_AGENT] [-c COOKIES] [-fs] [-e] [-p PROXY] [-q]
                [-o OUTPUT] [-s STATUS_CODES] [-U USERNAME] [-P PASSWORD]
                [-x EXTENSIONS]

optional arguments:
  -h, --help            show this help message and exit
  -w WORDLIST, --wordlist WORDLIST
                        path to wordlist
  -u URL, --url URL     address of remote site
  -t THREADS, --threads THREADS
                        number of threads to use
  -wf, --word-fuzz      shows response on basis of number of words
  -f, --force           use to force status check
  -a USER_AGENT, --user-agent USER_AGENT
                        add custom user agent
  -c COOKIES, --cookies COOKIES
                        pass cookies as a string
  -fs, --forward-slash  append a forward slash to all requests
  -e, --extended        show extended urls
  -p PROXY, --proxy PROXY
                        Proxy to use for requests [http(s)://host:port]
  -q, --quite           doesnt print banner and other stuff
  -o OUTPUT, --output OUTPUT
                        output to a file
  -s STATUS_CODES, --status-codes STATUS_CODES
                        manually pass the positive status codes (default
                        "200,204,301,302,307,403")
  -U USERNAME, --username USERNAME
                        username for basic http auth
  -P PASSWORD, --password PASSWORD
                        password for basic http auth
  -x EXTENSIONS, --extensions EXTENSIONS
                        file extension(s) to search for
```

## Examples
