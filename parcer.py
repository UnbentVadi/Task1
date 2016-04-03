from urllib.request import urlopen
from lxml.html import fromstring 
from lxml import cssselect

URL = "http://uacargo.com.ua/novaya-pochta/kiev"
item = ".material .text"
def parser():
	f = urlopen(URL)
	list_html = f.read().decode("utf-8")
	list_doc = fromstring(list_html)
	for eleb in list_doc.cssselect(item):
		a = eleb.cssselect("p")[5:]
		print(a)