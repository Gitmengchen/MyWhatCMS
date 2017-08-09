import requests
import hashlib
import glo



def MD5(data):
	m2 = hashlib.md5()
	m2.update(data)
	return m2.hexdigest()

def Check(url, tmp, data, step, j):
	for i in range(step * j,(step * (j + 1))):
		if(glo.FLAG == True):
			return 0
		url = tmp
		url = url + data[i]['url']
		try:
			r = requests.get(url)
		except:
			continue
		finally:
			if(data[i]['md5'] == ""):	
				code = r.status_code
				if(code == 200):
					re = r.text
					if(re.find(data[i]['re']) != -1):
						print(url)
						print(data[i]['name'])
						glo.FLAG = True
						break
			else:
				md5 = MD5(r.content)
				if(md5 == data[i]['md5']):
					print(url)
					print(data[i]['name'])
					break