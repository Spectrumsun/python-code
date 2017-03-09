
import urllib
from BeautifulSoup import *
import ssl

count = raw_input("Enter Count")
con = int(count)
position = raw_input("Enter position")
pos = int(position)

url = raw_input('Enter - ')
if len(url) < 1 : url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html"
taglist = list()
urllist = list()
urllist.append(url)

for i in range(con):
	soc = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
	data = urllib.urlopen(urllist[-1], context=soc).read()
	soup = BeautifulSoup(data)
	tags = soup('a')
	taglist = list()
	for tag in tags:
		taglist.append(tag)
	url = taglist[pos].get("href", None)
	print ("Retrieving: ', url"), urllist
	urllist.append(url)
print ("Last Url: ", urllist[-1])