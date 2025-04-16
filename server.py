import socket
import threading

HOST = '0.0.0.0'
PORT = 56789

clients = {}  # socket: username
topics = {}  # topic: list of usernames
subscriptions = {}  # username: list of topics

def broadcast(topic, message):
    if topic in topics:
        for username in topics[topic]:
            for sock, user in clients.items():
                if user == username:
                    try:
                        sock.sendall(f"[{topic}] {message}".encode('utf-8'))
                    except:
                        sock.close()

def handle_client(client_socket):
    username = client_socket.recv(1024).decode('utf-8')
    clients[client_socket] = username
    subscriptions[username] = []

    welcome = f"Welcome {username}! You can SUBSCRIBE, PUBLISH, LISTENERS, or TOPICS."
    client_socket.send(welcome.encode('utf-8'))

    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            if data.startswith("SUBSCRIBE"):
                _, topic = data.split(maxsplit=1)
                if topic not in topics:
                    topics[topic] = []
                if username not in topics[topic]:
                    topics[topic].append(username)
                    subscriptions[username].append(topic)
                    client_socket.send(f"Subscribed to topic: {topic}".encode('utf-8'))

            elif data.startswith("PUBLISH"):
                parts = data.split(maxsplit=2)
                if len(parts) < 3:
                    client_socket.send("Usage: PUBLISH <topic> <message>".encode('utf-8'))
                    continue
                _, topic, msg = parts
                broadcast(topic, f"{username}: {msg}")

            elif data.strip() == "TOPICS":
                topic_list = ", ".join(topics.keys()) if topics else "No topics available."
                client_socket.send(f"Topics: {topic_list}".encode('utf-8'))

            elif data.startswith("LISTENERS"):
                parts = data.split(maxsplit=1)
                if len(parts) < 2:
                    client_socket.send("Usage: LISTENERS <topic>".encode('utf-8'))
                    continue
                topic = parts[1]
                if topic in topics:
                    listeners = ", ".join(topics[topic])
                    client_socket.send(f"Listeners for {topic}: {listeners}".encode('utf-8'))
                else:
                    client_socket.send("Topic not found.".encode('utf-8'))

            else:
                client_socket.send("Invalid command.".encode('utf-8'))

        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()
    if client_socket in clients:
        del clients[client_socket]

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        print(f"New connection from {addr}")
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()
