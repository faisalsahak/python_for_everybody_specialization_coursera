import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

totalsum = 0
count = 0

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Url ')
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

commentsclass = soup.select('span[class="comments"]') 
numlist = list()
for comment in commentsclass:
    numlist.append(comment.get_text())

if len(numlist) > 0:
    for num in numlist:
        totalsum = totalsum + int(num)
        count = count + 1
print("Count :",count)
print("Total Sum :", totalsum)