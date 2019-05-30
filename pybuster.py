#!/usr/bin/pypy
from datetime import datetime
from random import choice
from string import ascii_lowercase,ascii_uppercase
from requests import get,head
from os import path
import threading
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-w","--wordlist", help="path to wordlist")
parser.add_argument("-u","--url", help="address of remote site")
parser.add_argument("-t","--threads", help="number of threads to use",default=20)
parser.add_argument("--auto",action="store_true",help="shows response on basis of number of words")
parser.add_argument("-f","--force",action="store_true",help="use to force status check")
parser.add_argument("-a","--user-agent", help="add custom user agent")
parser.add_argument("-c","--cookies", help="pass cookies as a string")
parser.add_argument("-fs","--forward-slash", help="append a forward slash to all requests",action="store_true")
parser.add_argument("-e","--extended", help="show extended urls",action="store_true")
parser.add_argument("-p","--proxy", help="Proxy to use for requests [http(s)://host:port]")
parser.add_argument("-q","--quite",action="store_true",help="doesnt print banner and other stuff")
parser.add_argument("-o","--output", help="output to a file")
parser.add_argument('-s','--status-codes',help='manually pass the positive status codes (default "200,204,301,302,307,403")')
parser.add_argument("-U","--username", help="username for basic http auth")
parser.add_argument("-P","--password", help="password for basic http auth")
parser.add_argument("-x","--extensions", help="file extension(s) to search for")
args = parser.parse_args()
extensions = None
if args.extensions != None:
	extensions = args.extensions.replace(' ','').replace(".",'').split(",")
	for i in range(len(extensions)):
		extensions[i] = '.'+extensions[i]
auth = ()
if args.username and args.password != None:
	auth = (args.username,args.password)
if args.output != None:
	f = open(args.output,"w+")
proxy = {}
if args.proxy != None:
	p = args.proxy
	if not p.startswith('http://') and not p.startswith('https://'):
		print "Proxy should be like [http(s)://host:port]"
		exit(1)
	proxy[p.split("://")[0]] = p
headers = {}
if args.user_agent != None:
	headers['User-Agent'] = args.user_agent
if args.cookies != None:
	headers['Cookie'] = args.cookies
valid = [200,204,301,302,307,403]
if args.status_codes != None:
	status_codes = args.status_codes.replace(' ','').split(",")
	valid = []
	for i in status_codes:
		valid.append(int(i))
vstr = []
for i in valid:
	vstr.append(str(i))
codes = ",".join(vstr)
def random_path():
	chars = ascii_lowercase+ascii_uppercase
	newstr = 'totallynotavalidpage'
	for i in range(15):
		newstr += choice(chars)
	return newstr

if args.wordlist != None:
	if not path.exists(args.wordlist):
		print "File Does Not Exist"
		exit(1)
	else:
		wordlist_name = args.wordlist
else:
	print "[+] Path to wordlist required!"
	parser.print_help()
	exit(1)
if args.url != None:
	base_url = args.url
	if not base_url.startswith('http://') and not base_url.startswith('https://'):
		base_url = 'http://'+base_url
	if not base_url.endswith('/'):
		base_url += '/'
else:
	print "[+] Not enough arguments, -u required"
	parser.print_help()
	exit(1)
wordlist = open(wordlist_name,'r').read().strip().splitlines()
w2 = wordlist
if args.extensions != None:
	for i in range(len(wordlist)):
		for j in extensions:
			w2.append(wordlist[i]+j)
if args.forward_slash:
	for i in range(len(wordlist)):
		if not wordlist[i].endswith('/'):
			wordlist[i] += "/"
thread_count = 20
if args.threads != None:
	try:
		thread_count = int(args.threads)
	except ValueError:
		print "[+] Please pass a number"

def find_s(wordlist):
	for i in wordlist:
            try:
		r = head(base_url+i,headers=headers,proxies=proxy,auth=auth)
		if r.status_code in valid:
			if not args.extended:
				print "/"+i+" (Status: %s)" %(r.status_code)
			else:
				print base_url+i+" (Status: %s)" %(r.status_code)
			if args.output != None:
				f.write(base_url+i+" (Status: %s)" %(r.status_code)+"\n")
            except:
                pass
def find_w(wordlist):
	path = random_path()
	r = get(base_url+path).content
	nw = len(r.split(' '))
	for i in wordlist:
            try:
		r = len(get(base_url+i,headers=headers,proxies=proxy,auth=auth).content.split(' '))
		r -= len(i.split(' '))-1
		if r != nw:
			if not args.extended:
				print "/"+i+" (Words: %s)" %(r)
			else:
				print base_url+i+" (Words: %s)" %(r)
			if args.output != None:
				f.write(base_url+i+" (Words: %s)" %(r)+"\n")
            except:
                pass
def chunk(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out
def check():
	if args.auto:
		return False
	if args.force:
		return True
	path = random_path()
	r = get(base_url+path)
	if r.status_code in valid:
		if not args.auto:
			print "[+] Wildcard response found /"+path+" ("+str(r.status_code)+")"
			print "[+] Use --auto for automatically showing available pages"
			print "[+] Use -f to force status code check"
		return False
	else:
		return True
ex = extensions
if args.extensions != None:
	if len(extensions) > 1:
		ex = ', '.join(extensions)
	else:
		ex = ''.join(extensions)
banner = """
=====================================================
Pybuster v1.0                                  by R4J
=====================================================
[+] Mode         : dir
[+] Url/Domain   : %s
[+] Threads      : %s
[+] Wordlist     : %s
[+] Status codes : %s
[+] Extensions   : %s
=====================================================
%s Starting pybuster
=====================================================""" %(base_url,thread_count,wordlist_name,codes,ex,datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
if not args.quite:
	print banner
w = chunk(w2,thread_count)
threads = []
if check():
	for i in w:
		x = threading.Thread(target=find_s, args=(i,))
		x.daemon = True
		threads.append(x)
		x.start()

elif args.auto:
        for i in w:
                x = threading.Thread(target=find_w, args=(i,))
                x.daemon = True
                threads.append(x)
                x.start()
for a,b in enumerate(threads):
	b.join()
fin = """=====================================================
%s Finished
=====================================================""" %(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
if not args.quite:
	print fin
if args.output != None:
	f.close()
