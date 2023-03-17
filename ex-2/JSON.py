import urllib.request
import json
import ssl

input = input('Enter URL:')
print('Retrieving:',input)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen(input, context = ctx).read()
print('Retrieved:',len(data),'charachters')
data = json.loads(data)
sum = 0
count =0

for item in data['comments']:
    sum += int(item['count'])
    count = count+1
print("count",count)
print('sum',sum)
