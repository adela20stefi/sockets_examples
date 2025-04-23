# Socket Examples – TCP & UDP

This repository contains simple Python socket examples using both **TCP** and **UDP**, to help understand the fundamental differences between the two transport layer protocols.

---

## Folder structure

```
sockets_ex/
├── TCP/
│   ├── server.py
│   └── client.py
└── UDP/
    ├── server.py
    └── client.py
```

---

## Detailed Documentation

- [TCP – details & usage](TCP/README.md)
- [UDP – details & usage](UDP/README.md)

---


## TCP vs UDP Comparison

| Feature               | TCP                          | UDP                         |
|-----------------------|-------------------------------|------------------------------|
| Connection            | Yes (3-way handshake)         | No                           |
| Acknowledgements      | Yes (ACKs)                    | No                           |
| Delivery Order        | Guaranteed                    | Not guaranteed               |
| Speed                 | Slower                        | Faster                       |
| Typical Applications  | Web, Email, FTP               | Streaming, VoIP, DNS         |



