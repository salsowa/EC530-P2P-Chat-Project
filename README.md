# EC530 P2P Chat Project

A terminal-based peer-to-peer messaging system built in Python using sockets and threading. This project demonstrates real-time communication between multiple clients through a central relay server.

---

## Features

- Asynchronous chat between multiple clients
- Users enter a username on connect
- Timestamped, JSON-formatted messages
- Server relays messages between clients
- Supports basic **publish/subscribe model**:
  - `SUBSCRIBE <topic>`: Join a topic
  - `PUBLISH <topic> <message>`: Send to all subscribers of a topic
  - `TOPICS`: View all published topics
  - `LISTENERS <topic>`: See who is subscribed to a topic
- No database or persistent storage required

## Technologies Used

- Python 3.x
- `socket` (built-in)
- `threading` (built-in)
- `json` (for message format)

## How to Run

### 1. Start the Server

Open a terminal and run:

```bash
python server.py
You should see:
Server is listening on 0.0.0.0:56789
New connection from ('127.0.0.1', xxxxx)
python client.py to run the client server

Once connected, you can type:
SUBSCRIBE <topic>
PUBLISH <topic> <message>
TOPICS
LISTENERS <topic>
Or send normal chat messages
Type exit to leave the chat

Example Chat Session
Terminal 1 — User: Sara

Enter your username: Sara
[Sara - 02:16 PM]: Hello, anyone online?
[Sara - 02:16 PM]: I'm just testing my P2P chat system.

Terminal 2 — User: Sam
Enter your username: Sam
[Sam - 02:17 PM]: Hi Sara, I can see it!

Example Command Usage
> SUBSCRIBE weather
> PUBLISH weather It's raining today.
> TOPICS
> LISTENERS weather




