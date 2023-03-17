import urllib.request
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URL = input('enter URL:')
XML = urllib.request.urlopen(URL,context = ctx).read()
print('Retrieving:', URL)

tree = ET.fromstring(XML)
counts = tree.findall('.//count')
sum = 0

for i in counts:
    sum = sum+ int(i.text)

print(sum)
