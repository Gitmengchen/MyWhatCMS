import requests
import hashlib
import re
from DATA import CMSDATA
from config import *
class WhatCMS(object):
	"""docstring for WhatCMS"""
	def __init__(self, url):
		super(WhatCMS, self).__init__()
		self.url = url

	def Judge(self, data):#传入一条CMS指纹 data 并进行判断，返回结果
		Url = self.url + data['url']
		try:
			res = requests.get(Url,headers=headers)
		except:
			return ""
		if res.status_code == 200:
			if data['md5']:
				#进行 MD5 识别
				md5 = self.MD5(data=res.content)
				if md5 == data['md5']:
					return data['name']
			else:
				#进行 内容匹配 识别
				if self.Search(data['re'], res.text):
					return data['name']
		return ""

	def MD5(self, data):
		return hashlib.md5(data).hexdigest()

	def Search(self, regex, content):#内容匹配
		if re.search(regex, content):
			return True
		return False

		