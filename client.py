import socket
import threading
import sys

# Ask for username
username = input("Enter your username: ")

# Server configuration
SERVER_IP = '127.0.0.1'
PORT = 56789  # Must match the server's port

def receive_messages(client_socket):
    """Continuously receives messages from the server and displays them."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print("\n" + message)
        except:
            break

def start_client():
    """Connects to the server and starts sending messages."""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, PORT))

        threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

        print("Connected to chat. Type your message and press Enter to send.")
        print("Type 'exit' to leave the chat.")

        while True:
            message = sys.stdin.readline().strip()
            if message.lower() == "exit":
                print("Disconnecting...")
                break
            full_message = f"[{username}]: {message}"
            client_socket.send(full_message.encode('utf-8'))

        client_socket.close()

    except ConnectionRefusedError:
        print("Could not connect to server. Make sure the server is running.")

if __name__ == "__main__":
    start_client()
