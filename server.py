import socket
import threading
import sqlite3
from datetime import datetime

# Server configuration
HOST = '0.0.0.0'
PORT = 56789

clients = []  # List of connected client sockets

# Save messages to SQLite database
def save_message_to_db(username, message):
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    message TEXT,
                    timestamp TEXT
                )''')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO messages (username, message, timestamp) VALUES (?, ?, ?)",
              (username, message, timestamp))
    conn.commit()
    conn.close()

# Handle messages from one client
def handle_client(client_socket, address):
    print(f"New connection from {address}")
    clients.append(client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)

            # Try to extract username for saving to DB
            try:
                username_part, actual_message = message.split("]: ", 1)
                username = username_part.replace("[", "").split(" |")[0]
                save_message_to_db(username, actual_message)
            except:
                pass

            # Broadcast to other clients
            for client in clients:
                if client != client_socket:
                    client.sendall(message.encode('utf-8'))

        except:
            break

    print(f"Connection closed: {address}")
    clients.remove(client_socket)
    client_socket.close()

# Server input loop to send messages to all clients
def server_input_loop():
    while True:
        message = input()
        if message.lower() == "exit":
            print("Server is shutting down message sender.")
            break
        timestamp = datetime.now().strftime("%I:%M %p")
        full_message = f"[Server | {timestamp}]: {message}"
        print(full_message)
        for client in clients:
            try:
                client.sendall(full_message.encode('utf-8'))
            except:
                pass

# Start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server is listening on {HOST}:{PORT}")

    # Start thread for server to send messages
    threading.Thread(target=server_input_loop, daemon=True).start()

    while True:
        client_socket, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

if __name__ == "__main__":
    start_server()
