import json
import urllib

js = raw_input ("Enter url")
if len(js) < 1 : js = "http://python-data.dr-chuck.net/comments_42.json"
url = urllib.urlopen(js)
data = url.read()
info = json.loads(data)

for item in info:
	print 'name', item['count']

