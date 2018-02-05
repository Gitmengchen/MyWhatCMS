#coding:utf-8
import json
import queue

CMSDATA = queue.Queue()

with open('data.json', 'r') as file:#读取数据
		data = json.load(file)
for i in range(len(data)):#将数据放在队列CMSDATA里
	CMSDATA.put(data[i])

