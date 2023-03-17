from bs4 import BeautifulSoup
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1079224.html',context = ctx).read()
soup = BeautifulSoup(url,'html.parser')

tags = soup('span')
sum = 0

for tag in tags:
    sum += int(tag.contents[0])

print(sum)
