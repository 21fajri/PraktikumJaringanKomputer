from socket import *
import threading 
def handle_client(connectionSocket):
    try :
        # menerima pesan user
        # 10101100 = "message"
        message = connectionSocket.recv(1024).decode()
        
        message = message[4:15]
        print(message)
        # index.html, hello.html
        # message = /GET index.html HTTP/1.1
        # filename = message.split()[1]
        
        # membuka index.html serta menghilangkan "/"
        f = open(message[1:])
        
        # membaca file html
        outputData = f.read()
        
        # mengirim respons
        connectionSocket.send(
            "HTTP/1.1 200 OK\r\n\r\n".encode()
        )
        
        # kirim data
        connectionSocket.sendall(outputData.encode()) 
        
        # close connection
        connectionSocket.close()
    except IOError :
        # kirim pesan
        connectionSocket.send(
            "HTTP/1.1 404 Not Found\r\n\r\n".encode()
        )
        
        # kirim data
        connectionSocket.send(
            "<h1>404 Not Found</h1>".encode()
        )
        
        # tutup koneksi
        connectionSocket.close()
        
serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.bind(('', 6789))
serversocket.listen(5) # dapat menerima sebanyak 5 client
print("[Server] System is running ... ")

while True :
    connectionSocket,addr = serversocket.accept()    

    # Membuat thread dan target threadnya, beserta parameter
    thread = threading.Thread(
        target = handle_client,
        args = (connectionSocket,)
    )
    # menjalankan
    thread.start()
