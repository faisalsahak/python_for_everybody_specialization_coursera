import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL : ')
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

countinp = input('Enter count : ')
count = int(countinp)

positioninp = input('Enter position : ')
position = int(positioninp)

currcount = 0

while currcount < count :
	
	tags = soup('a')
	for tag in tags:
		tag = tags[position - 1].get('href', None)
	print("Retrieving : " + tag)
	
	url = tag
	html = urllib.request.urlopen(url, context = ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	
	currcount = currcount + 1