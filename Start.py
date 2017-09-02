#!python3
#-*-coding:utf-8-*-

import json
import threading
#自写库
import WhatCMS

if __name__ == '__main__':
	with open('data.json', 'r') as file:#读取数据
		data = json.load(file)

	print("库中共有%d条指纹" % len(data))
	print("推荐线程数为10")

	url = input("输入url\n")
	tmp = url
	th = input("输入线程数\n")
	step = int(len(data)/int(th))

	threads = []
	for j in range(int(th)):#创建多线程
		t = threading.Thread(target=WhatCMS.Check,args=(url,tmp,data,step,j))
		threads.append(t)
	t = threading.Thread(target=WhatCMS.Check,args=(url,tmp,data,step,int(th)))
	threads.append(t)

	for i in range(len(threads)):
		threads[i].start()




