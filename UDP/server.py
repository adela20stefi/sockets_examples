import socket

# create UDP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to the specified IP address and port
server_address = ('127.0.0.1', 1234)
server_socket.bind(server_address)
print("UDP Server listening on 127.0.0.1:1234...")

# receive data loop
while True:
    data, addr = server_socket.recvfrom(1024)  # buffer size is 1024 bytes
    print(f"Received message: {data.decode()} from {addr}")

    # send response back to the client
    response = "Hello from the UDP server!"
    server_socket.sendto(response.encode(), addr)