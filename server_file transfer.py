import socket
b = open(input('enter file name:').replace('"',''),'rb').read()
c = bytes(input('enter file type(any HTTP valid content-type eg.text/plain):'),'UTF-8')
serversocket = socket.socket()
serversocket.bind((socket.gethostbyname(socket.gethostname()),8000))
serversocket.listen(1)
print('Access http://'+socket.gethostbyname(socket.gethostname())+':8000 connected to same network as this machine')
print('waiting.....\n')
while(1):
    conn,a =serversocket.accept()
    data = conn.recv(1024).decode()
    if not data:
        continue
    if data.split('\n')[0] == 'GET /favicon.ico HTTP/1.1\r':
        continue
    print(data)
    sd = b'HTTP/1.1 200 OK\r\n Content-type:'+c+b'\r\n\r\n'+b
    conn.send(sd)
    conn.close()
    print('waiting.....\n')
