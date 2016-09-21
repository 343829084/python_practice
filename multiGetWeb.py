#coding=utf8

import urllib2
import time
from threading import Thread

class GetUrlThread(Thread):
	def __init__(self, url, threadId):
		self.url = url
		self.threadId = threadId
		super(GetUrlThread, self).__init__()

	def run(self):
		resp = urllib2.urlopen(self.url)
		print("threadId[%s] start, get result:=%s " % (self.threadId, resp.getcode()))

if __name__ == "__main__":
	url = "http://192.168.65.128:3000"
	threads = []
	for i in range(10):
		th = GetUrlThread(url, i)
		threads.append(th)
	for t in threads:
		t.start()
		t.join()

	print("system close!")

