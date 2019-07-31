import socket

# Create a socket which takes ipv4 address and is TCP oriented:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1357 #any number
s.bind((socket.gethostname(), port))#bind socket to local host and port

s.listen(8)

conn, address = s.accept()
print(f"Connection from {address} is done.")

while True:

    try:
        data = conn.recv(1024) # receive data from client

        if not data: break

        print(data)
        conn.send(bytes("Server received your connection message!","utf-8")) 
    except socket.error:
        print("Error Occured.")
        break

conn.close()
