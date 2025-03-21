import socket
import threading

# Server configuration
HOST = '0.0.0.0'
PORT = 56789

clients = []  # To keep track of connected clients

def handle_client(client_socket, address):
    """Receives messages from a client and broadcasts to others."""
    print(f"New connection from {address}")
    clients.append(client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{message}")
            for client in clients:
                if client != client_socket:
                    client.sendall(message.encode('utf-8'))
        except:
            break

    print(f"Connection closed: {address}")
    clients.remove(client_socket)
    client_socket.close()

def start_server():
    """Starts the chat server and listens for connections."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server is listening on {HOST}:{PORT}")

    while True:
        client_socket, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

if __name__ == "__main__":
    start_server()
