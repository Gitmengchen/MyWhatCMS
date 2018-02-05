import threading
import queue
from DATA import CMSDATA
from WhatCMS import WhatCMS
import time
import argparse
import sys

RESULT = queue.Queue() 

def echo():# 处理并输出结果
	result = []
	while not RESULT.empty():
		result.append(RESULT.get())
	if result:
		tmp = set(result)
		print("%d be matched" % len(tmp))
		for i in tmp:
			print(i)
	else:
		print("No matching fingerprints")



def Run(url):# 进行扫描
	cms = WhatCMS(url)
	while not CMSDATA.empty(): 
		data = CMSDATA.get()
		result = cms.Judge(data=data)
		#print(CMSDATA.qsize())
		if result:
			RESULT.put(result)
			break
def main(url):
	time1 = time.time()
	threads = []
	for j in range(10):#创建多线程
		t = threading.Thread(target=Run,args=(url,))
		threads.append(t)
	for i in range(len(threads)):
		threads[i].start()
	for i in range(len(threads)):
		threads[i].join()
	echo()
	print(time.time() - time1)

if __name__ == '__main__':
	paraser = argparse.ArgumentParser(description="WhatCMS Ver:1.0")
	paraser.add_argument("-u", "--url", metavar="", help="Web url")
	args = paraser.parse_args()

	try:
		url = args.url
		if not url:
			print("Usage: run.py -u http://www.test.com")
			sys.exit(1)
		main(url)
	except KeyboardInterrupt:
		sys.exit(1)
	