import urllib.request
from bs4 import BeautifulSoup
import ssl
import re

URL = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position'))

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(URL,context= ctx).read()

for i in range(count):
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    URL = tags[position-1].get('href')
    html = urllib.request.urlopen(URL,context= ctx).read()
    print('Retrieving:',URL)
