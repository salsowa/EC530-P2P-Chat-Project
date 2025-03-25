import socket
import threading
import sys
from datetime import datetime

# Ask for username
username = input("Enter your username: ")

# Server configuration
SERVER_IP = '127.0.0.1'
PORT = 56789  # Must match the server's port

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print("\n" + message)
        except:
            break

# Function to start the client
def start_client():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, PORT))

        # Start background thread to receive messages
        threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

        print("Connected to chat. Type your message and press Enter to send.")
        print("Type 'exit' to leave the chat.")

        # Send messages
        while True:
            message = sys.stdin.readline().strip()
            if message.lower() == "exit":
                print("Disconnecting...")
                break
            timestamp = datetime.now().strftime("%I:%M %p")
            full_message = f"[{username} | {timestamp}]: {message}"
            client_socket.send(full_message.encode('utf-8'))

        client_socket.close()

    except ConnectionRefusedError:
        print("Could not connect to server. Make sure the server is running.")

if __name__ == "__main__":
    start_client()
