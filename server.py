import socket

HOST = "0.0.0.0"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"VPN server started on port {PORT}")

while True:
    client, address = server.accept()
    print(f"Connection from {address}")

    client.sendall(b"Hermes VPN server\n")
    client.close()
