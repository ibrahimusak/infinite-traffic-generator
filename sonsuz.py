#!/usr/bin/python
from subprocess import Popen
import os,sys
import time
filename = sys.argv[1]
a = 0
while True:
	while a<=10:
		print("islem yeniden basladi")
		os.system("killall Xvfb")
		os.system("killall webkit_server")
		p = Popen("python " + filename, shell=True)     
		p.wait()
		a += 1
	while a>10:
		print("proxy toplaniyor")
		os.system("killall Xvfb")
		os.system("killall webkit_server")
		p = Popen("python3 "+"proxy.py",  shell=True)     
		p.wait()
		a -=10
