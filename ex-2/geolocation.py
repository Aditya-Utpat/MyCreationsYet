import urllib.request, urllib.parse
import ssl
import json

api_key = False

if api_key is False:
    API = 'http://py4e-data.dr-chuck.net/json?'
else:
    API = 'https://maps.googleapis.com/maps/api/geocode/json?'
    api_key=42
    
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter address')
parms = dict()
parms['address']= address
parms['key']=api_key
URL = API +urllib.parse.urlencode(parms)
print('Retrieving:',URL)
URL = urllib.request.urlopen(URL).read()
print('Retrieved',len(URL))

json1 = json.loads(URL)
print('place_id',json1['results'][0]['place_id'])
