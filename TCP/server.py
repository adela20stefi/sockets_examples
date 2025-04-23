import socket

# create TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the specified IP address and port
server_address = ('127.0.0.1', 1234)
server_socket.bind(server_address)

# listen for incoming connections
server_socket.listen(1)
print("Server listening on 127.0.0.1:1234...")

# accept client connections
while True:
    client_socket, addr = server_socket.accept()
    print(f"Received connection from {addr}")

    data = client_socket.recv(1024)
    print(f"Received data: {data.decode()}")

    # send a message back to the client
    response = "Hello, client! Your message was received."
    client_socket.sendall(response.encode())

    client_socket.close()