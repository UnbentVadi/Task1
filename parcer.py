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
		text_site = [content_site.text_content() for content_site in a]
		myStringSite = ''.join(text_site)
	return myStringSite

def write_file(string_text):
	f = open("main.html", "w", encoding="utf-8")
	#with open("main.html", "w", encoding="utf-8") as f:
	f.write(u"<p>"+string_text+"</p>")
	f.close() 

def main():
	string_text = parser()
	write_file(string_text)

if __name__ == "__main__":
	main()