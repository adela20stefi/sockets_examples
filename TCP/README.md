# TCP – Socket Client & Server

## Description

TCP (Transmission Control Protocol) is a **connection-oriented** transport layer protocol. It ensures that data is delivered **reliably**, **in order**, and **without duplication**. TCP is widely used for applications that require complete data integrity.

Typical use cases for TCP include:
- Web browsing (HTTP/HTTPS)
- Email (SMTP, IMAP, POP3)
- File transfer (FTP)
- Remote administration (SSH)

---

## How to Run

Open **two terminals**:

**Terminal 1 (Server):**
```bash
python server.py
```

**Terminal 2 (Client):**
```bash
python client.py
```

---

## How It Works

- The server binds to 127.0.0.1:1234, listens for incoming connections, and accepts a client.
- The client connects to the server via TCP.
- The client sends a message.
- The server receives the message and sends a confirmation message back.
- The client displays the server's response and closes the connection.

TCP uses a 3-way handshake (`SYN → SYN-ACK → ACK`) to establish the connection before any data is exchanged.

| Client                     | Server                   |                                                |
|----------------------------|--------------------------|------------------------------------------------|
| SYN →                      |                          | (Step 1: Client says "I want to talk")         |
|             | ← SYN + ACK              | (Step 2: Server says "Okay, I’m listening")    |
| ACK →                      |                          | (Step 3: Client says "Thanks, let’s start")    |
---

## Back to Main Docs

🔙 [Return to main documentation](../README.md)
