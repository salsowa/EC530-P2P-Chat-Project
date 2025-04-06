import socket
import threading

# Server configuration
HOST = '0.0.0.0'
PORT = 56789

clients = []

# Broadcast message to all clients
def broadcast(message, sender_socket=None):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                clients.remove(client)

# Handle individual client connection
def handle_client(client_socket, address):
    print(f"New connection from {address}")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)  # show in server terminal
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

# Start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server is listening on {HOST}:{PORT}")
    while True:
        client_socket, address = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

if __name__ == "__main__":
    start_server()
