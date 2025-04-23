# UDP – Socket Client & Server

## Description

UDP (User Datagram Protocol) is a **connectionless** transport layer protocol. It provides **fast** communication with **no guarantee of delivery, order, or error correction**. This makes it ideal for applications where speed is more important than reliability.

Typical use cases for UDP include:
- Online games
- Voice over IP (VoIP)
- Video streaming
- DNS lookups

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

- The server binds to `127.0.0.1:1234` and listens for incoming UDP messages.
- The client sends a UDP message to the server.
- The server receives the message and sends a reply back to the client.
- The client prints the server's response and closes the socket.

Unlike TCP, there is no handshake or persistent connection. Each UDP packet is independent and may be lost or arrive out of order.

UDP is **connectionless** and does **not guarantee** delivery or order. It's fast, lightweight, and perfect for real-time communication like games or streaming.


| Client                     | Server                   |                                              |
|----------------------------|--------------------------|----------------------------------------------|
| Message →                  |                          | (Client sends datagram to server)            |
|                            | ← Response               | (Server replies to the received message)     |
---

## Back to Main Docs

🔙 [Return to main documentation](../README.md)
