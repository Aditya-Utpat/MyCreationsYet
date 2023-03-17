from socket import *
import re
def createServer():
    inp = input('Enter text:')
    serversocket = socket(AF_INET, SOCK_STREAM)
    try :
        serversocket.bind(('192.168.0.104',10000))
        serversocket.listen(5)
        while(1):
            (clientsocket, address) = serversocket.accept()
            rd = clientsocket.recv(5000).decode()
            print(rd)
            #rd = rd.split()
            #if not rd[1][1:] == 'favicon.ico':print(rd[1][1:])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += '<html><body size="2cm">'+inp+"</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt :
        print("\nShutting down...\n")
    except Exception as exc :
        print("Error:\n")
        print(exc)

    serversocket.close()

print('Access http://localhost:9000')
createServer()
