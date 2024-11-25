import sqfite3
import requests
from bs4 import BeautifulSoup
orel ="https://quotes.toscrape.com/"
r = requests.get (orel)
s = BeautifulSoup(r.text,"lxml")
q = soup.find_all("span", class_="text")
a = soup.find_all("small", class_="author")
tags = soup.find_all("div", class_="tags")
for t in tags:
	print(t.text.split()[1:])

conn sqfite3.connect("C:\\Users\\1024\\Desktop\\сп10")
