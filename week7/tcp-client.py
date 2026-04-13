from socket import *

servername = "localhost"
serverport = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((servername, serverport))

print("[SYSTEM] Masukkan pesan ")

running = True
while running:
    message = input("> ")
    clientSocket.send(message.encode())
    
    if message.lower() == "exit":
        print("[SYSTEM] Keluar dari program")
        running = False
        break
    
    modifiedMessage = clientSocket.recv(2048)
    print("[SERVER] pesan : ", modifiedMessage.decode())

clientSocket.close()
print("[SYSTEM] Koneksi ditutup")