# Complete Networking Fundamentals

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Definitions](#definitions)
- [OSI Layer](#osi-layer)
- [Binary, Decimal, Hexadecimal](#binary-decimal-hexadecimal)
- [IPv4](#ipv4)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Definitions

- Computer Network
- Network Protocol
- Home network: - Internet - Modem - Router - Switches - laptop, desktop, phones
- **SOHO**: Small office and Home office: - Internet - Wireless firewall / Router - Switches - Printer - Computer
- **IP** Address: Internet Protocol Address
- **DNS**: Domain Name System

## OSI Layer

> All people sleeping through networking don't pass

Advantages:

- standard
- split development
- interoperability
- faster development

CLNS:

- Application (Layer 7)
- Presentation (Layer 6): JPEG, HTML
- Session (Layer 5)
- Transport (Layer 4) via segments: `TCP`, `UDP`
- Network (Layer 3) via packets: `OSPF`, `BGP`, `IS-IS` using routers
- Data Link (Layer 2) via frames: `MAC`
- Physical (Layer 1) via bits: Copper, Fibre, Wireless

Encapsulation and then De-Encapsulation across all layers

TCP/IP:

- Application (1st 3 layers in OSI)
- Transport
- Internet (Network later in OSI)
- Network access (last 2 layers in OSI)

Hybrid:

- Application (1st 3 layers in OSI)
- Transport
- Network
- Data Link
- Physical

## Binary, Decimal, Hexadecimal

Uses:

- Subnetting
- Access lists
- Inverting IP addressees

| Base ^ Exponent | `2^7` | `2^6` | `2^5` | `2^4` | `2^3` |
| ------ | ------ | ------ | :----- | ------ | ------ |
| Binary | 1 | 1 | 1 | 1 | 1 |
| Decimal | 128 | 64 | 32 | 16 | 8 |

## IPv4

- Layer 3 in OSI layer
- Connectionless protocol
- Depends on higher level protocol `TCP` with 3-way handshake: `SYN`, `SYN/Ack`, `Ack`
- Packet routing depending on load balancing, bandwidth, hop counts
- Best effort delivery
- 32 bits, 4 octets
