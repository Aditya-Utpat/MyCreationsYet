from http.server import HTTPServer, BaseHTTPRequestHandler,SimpleHTTPRequestHandler
import re
from socket import gethostname, gethostbyname
import urllib.parse
import os
import sys
from http import HTTPStatus
import html
import io

class HTTPRequestHandler(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        try:
            list = os.listdir(path)
        except OSError:
            self.send_error(
                HTTPStatus.NOT_FOUND,
                "No permission to list directory")
            return None
        list.sort(key=lambda a: a.lower())
        r = []
        try:
            displaypath = urllib.parse.unquote(self.path,
                                               errors='surrogatepass')
        except UnicodeDecodeError:
            displaypath = urllib.parse.unquote(path)
        displaypath = html.escape(displaypath, quote=False)
        enc = sys.getfilesystemencoding()
        title = 'Directory listing for %s' % displaypath
        r.append('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
                 '"http://www.w3.org/TR/html4/strict.dtd">')
        r.append('<html>\n<head>')
        r.append('<meta http-equiv="Content-Type" '
                 'content="text/html; charset=%s">' % enc)
        r.append('<title>%s</title>\n</head>' % title)
        r.append('<body>\n<h1>%s</h1>' % title)
        r.append('<hr>\n<ul>')
        for name in list:
            fullname = os.path.join(path, name)
            displayname = linkname = name
            # Append / for directories or @ for symbolic links
            if os.path.isdir(fullname):
                displayname = name + "/"
                linkname = name + "/"
            if os.path.islink(fullname):
                displayname = name + "@"
                # Note: a link to a directory displays with @ and links with /
            r.append('<li><a href="%s">%s</a></li>'
                    % (urllib.parse.quote(linkname,
                                          errors='surrogatepass'),
                       html.escape(displayname, quote=False)))
        r.append('''</ul>\n<hr>\n</body>\n</html>\n
                <form action="uploader.php" method="POST" enctype="multipart/form-data">
                <input type="file" name="fileToUpload" id="fileToUpload">
                <input type="submit" value="Upload" name="submit">
                </form>''')
        encoded = '\n'.join(r).encode(enc, 'surrogateescape')
        f = io.BytesIO()
        f.write(encoded)
        f.seek(0)
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        return f


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
        x = self.path.replace('/','\\')
        x = x.replace('\\uploader.php','')
        if x == '\\': x = ''
        filepath = os.getcwd() + x +'\\'
        a = open(filepath+filename,'wb')
        a.write(body)
        a.close()
        #saves the content to file
IP = gethostbyname(gethostname())                        # gets IP of computer
print('Open@http://'+IP+':8000')
httpd = HTTPServer((IP, 8000),HTTPRequestHandler)        # binds to the IP at port 8000 (Python may need some OS permissions)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print('Server stopped due to Keyboard Interrupt')
    sys.exit(0)
