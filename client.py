import socket
import threading
import sys
from datetime import datetime
import json

# Ask for username
username = input("Enter your username: ")

# Server configuration
SERVER_IP = '127.0.0.1'
PORT = 56789

# Receive messages
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print("\n" + message)
        except:
            break

# Start client
def start_client():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, PORT))

        threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

        print("Connected to chat. Type your message and press Enter to send.")
        print("Type 'exit' to leave the chat.\n")

        while True:
            message = sys.stdin.readline().strip()
            if message.lower() == "exit":
                print("Disconnecting...")
                break

            data = {
                "type": "chat",
                "sender": username,
                "timestamp": datetime.now().isoformat(),
                "payload": {
                    "message": message
                }
            }

            client_socket.send(json.dumps(data).encode('utf-8'))

        client_socket.close()

    except ConnectionRefusedError:
        print("Could not connect to server. Make sure the server is running.")

if __name__ == "__main__":
    start_client()
