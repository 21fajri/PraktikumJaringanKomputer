from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

serverSocket.listen(1)
print("[SYSTEM] Server siap menerima koneksi")

running = True

while running:
    connectionSocket, addr = serverSocket.accept()
    while True:
        message = connectionSocket.recv(2048).decode()
        if not message:
            break

        if message.lower() == "exit":
            print("[SYSTEM] Client ingin keluar")
            running = False
            break
        
        modifiedMessage = message.upper()   
        print("[CLIENT] pesan : ", message)
        connectionSocket.send(modifiedMessage.encode())
    connectionSocket.close()
serverSocket.close()
print("[SYSTEM] Server ditutup")