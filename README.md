# EC530 P2P Chat Project
A terminal-based peer-to-peer messaging system built in Python using sockets and threading. This project demonstrates basic chat functionality between clients through a central relay server.
## Features
- Asynchronous chat between multiple clients
- Each user enters a username when they join
- Timestamped messages
- JSON message formatting
- Server relays messages between clients 
- No database or persistent storage required 
## Technologies Used
- python 3.x
- socket (built-in)
- threading (built-in)
- JSON (for message structure)
## How to Run
### 1. Start the Server

Open a terminal and run:
python server.py
*You should see:
Server is listening on 0.0.0.0:56789
New connection from ('127.0.0.1', xxxxx)

**Start Clients
Open a separate terminal for each user:
python client.py

Example Chat Session
Terminal 1 — User: Sara
Enter your username: Sara

[Sara - 02:16 PM]: Hello, anyone online?
[Sara - 02:16 PM]: I'm just testing my P2P chat system.
User: Sam
Enter your username: Sam

{"type": "chat", "sender": "Sara", "timestamp": "2025-04-06T14:16:01.547383", "payload": {"message": "Hello, anyone online?"}}

{"type": "chat", "sender": "Sara", "timestamp": "2025-04-06T14:16:50.093452", "payload": {"message": "I'm just testing my P2P chat system"}}

[Sam - 02:17 PM]: Hi Sara, I can see it!
