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
- Graceful exit using `exit` command

---

## How to Run

### 1. Run the Server
```bash
python server.py
-You should see: Server is listening on 0.0.0.0:56789
### 1. Run the Client in a seprate terminal
```bash
Python client.py

You’ll be prompted for a username:
Enter your username:
Then you can begin chatting:
Example
[Ali]: Hello!
[Sara]: Hi Ali!



