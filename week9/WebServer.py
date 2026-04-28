from socket import *
import sys 

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print(f"[SERVER] Berjalan di port {serverPort}...")

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()        
        if not message:
            continue            
        filename = message.split()[1]        
        f = open(filename[1:])        
        outputdata = f.read()        
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())        
        connectionSocket.send("Content-Type: text/html\r\n".encode())        
        connectionSocket.send("\r\n".encode())        
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())        
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
        print(f"File {filename} berhasil dikirim.")

    except IOError:
        print(f"File {filename} tidak ditemukan.")
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send("404 Not Found\r\n".encode())        
        connectionSocket.close()
    
    serverSocket.close()
    sys.exit()