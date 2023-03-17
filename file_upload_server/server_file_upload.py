'''
Created by Aditya Utpat

This program creates a basic HTTP server. The server can be accessed by any devices on the Local network.
When accessed through browser it displays a HTML page with a form to upload a file.
The server saves the file in the host system and asks the client for another upload.

Requirs - Python3 , upload.html , uploader.php
run the script in same directory as the above mentioned files
may need some network permissions in OS to be turned on for python
'''

from http.server import HTTPServer, BaseHTTPRequestHandler # this modules creates a very basic HTTP server
from socket import gethostname, gethostbyname # needed to get the system IP
import re   # needed to seperate filename from body

upload_page = open('upload.html','rb').read()  #opens the HTML page
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(upload_page)
        #tells the server what to do on GET request
        #sends the HTML upload page
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        webkitboundary = self.headers['Content-Type'][30:].replace('-','')
        #gets the content of uploaded file
        self.send_response(200)
        self.end_headers()
        # sends a 200 OK reponse header
        response = b'<!DOCTYPE html><a href="http://'+bytes(IP,'UTF-8')+b':8000">upload another file? </a>'
        self.wfile.write(response)
        # sends a small HTML script above
        str_body = str(body)
        filename = re.findall('filename="(.+?)"',str_body)[0]
        #retracts filename from body
        webkitboundary = re.findall('-+'+webkitboundary,str_body)[0]
        body = body[len(webkitboundary)+len(filename)+66:]
        body = body[0:0-(len(webkitboundary)*2+63)]
        contenttype = re.findall(b'Content-Type: .+?\r\n',body)[0]
        body = body[4+len(contenttype):]
        #removes webkitboundary header from body
        print('saving',filename)
        a = open(filename,'wb')
        a.write(body)
        a.close()
        #saves the content to file

IP = gethostbyname(gethostname())                        # gets IP of computer
print('Open@http://'+IP+':8000')
httpd = HTTPServer((IP, 8000), SimpleHTTPRequestHandler) # binds to the IP at port 8000 (Python may need some OS permissions)
httpd.serve_forever()                                    # starts the server
