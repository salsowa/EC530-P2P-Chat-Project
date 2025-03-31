# EC530 Chat Project – Phase 1

## Overview
This project is a command-line based peer-to-peer chat system implemented using Python. It allows multiple clients to connect to a server and exchange messages in real-time.

Phase 1 focuses on the basic chat functionality and asynchronous communication.

---

## Features
- Real-time messaging between multiple clients
- Asynchronous send/receive using `threading`
- Server relays messages to all connected users
- User-defined usernames for clean message display
- Timestamps added to all messages
- SQLite database logs all chat messages
- Server can now send messages (full duplex)
-  system now uses a structured JSON message protocol to support automation, machine-readability, and future integrations (e.g., notifications, REST APIs, or logging).

---#### Example Message Format:
```json
{
  "type": "chat",
  "sender": "Sara",
  "timestamp": "2025-03-31T17:12:08.729705",
  "payload": {
    "message": "im having lunch"
  }
}

# How to Run the Chat System

### Requirements

- Python 3 installed (no extra libraries needed)
- SQLite3 (already built-in with Python)
- Command-line or terminal access

---

### 1. Start the Server

Open a terminal and navigate to your project folder:

```bash
cd EC530-chat\ project
python server.py
- You'll see: Server is listening on 0.0.0.0:56789
Then, in a new terminal Start the Client
run the client it will ask : Enter your username:
Then start typing messages. Messages will appear like:

[Server} | 03:45 PM]: Hello!
[Sara | 03:46 PM]: Hey!


-- Chat history is stored in python view_db.py
example: 
(1, 'Chi', 'Hello!', '2025-03-25 15:42:10')
(2, 'Sara', 'Hi Chi!', '2025-03-25 15:43:01')
(1, 'Server', 'Hi!', '2025-03-25 15:42:10')
