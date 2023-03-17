import socket
b = input('enter text:')
serversocket = socket.socket()
serversocket.bind((socket.gethostbyname(socket.gethostname()),8000))
serversocket.listen(1)
print('Access http://'+socket.gethostbyname(socket.gethostname())+':9000 connected to same network as this machine')
print('waiting.....\n')
while(1):
    conn,a =serversocket.accept()
    data = conn.recv(1024).decode()
    if not data:
        continue
    if data.split('\n')[0] == 'GET /favicon.ico HTTP/1.1\r':
        continue
    print(data)
    sd = 'HTTP/1.1 200 OK \r\nContent-Type: text/plain\r\n\r\n'+b
    conn.send(sd.encode())
    conn.close()
    print('waiting.....\n')
