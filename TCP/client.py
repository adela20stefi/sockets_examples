import socket

# create TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set the source address for the socket
source_address = ('127.0.0.1', 0)
client_socket.bind(source_address)

# connect to the server
server_address = ('127.0.0.1', 1234)
client_socket.connect(server_address)

# send data to the server
client_socket.sendall(b'Hello, server! This is client 127.0.0.1')

# receive response from the server
response = client_socket.recv(1024)
print(f"Received from server: {response.decode()}")

# close the socket
client_socket.close()