import dryscrape
import time
import os,sys
import threading
from threading import Thread
import random
from random_useragent.random_useragent import Randomize
import webkit_server
import gc
r_agent = Randomize()
useragent = r_agent.random_agent('smartphone','ios')
url = "write your website"
def main():
	try:
		with open("proxy.txt") as f:
			lines = f.readlines()
			proxy = random.choice(lines)
			ip, port = proxy.split(':')
		server = webkit_server.Server()
		server_conn = webkit_server.ServerConnection(server=server)
		driver = dryscrape.driver.webkit.Driver(connection=server_conn)			
		sess = dryscrape.Session(driver=driver)
		sess.set_proxy(ip,port)
		sess.set_header('User-Agent', useragent)
		sess.set_timeout(15)
		sess.visit(url)
		print("girdi hacii")
		from random import randint
		from time import sleep
		sleep(randint(10,20))
		gc.collect()
	except:
		pass
try:	
	dryscrape.start_xvfb()
except:
	os._exit(1)

if __name__ == '__main__':
    for t in range(50):
        t = threading.Thread(target=main)
        t.start()
	

