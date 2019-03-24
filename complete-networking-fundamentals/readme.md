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
- Address classes replaced by CIDR in 1993
- Local loopback addresses: `127.0.0.1` or `127.X.Y.Z`
- Router's loopback addresses: `10.1.1.1/32`
- Link local addresses: `169.254.0.0/16`

Class addresses prior to 1993 `W.X.Y.Z`

| Class | Net ID | Subnet mask | 1st Octet | 2nd Octet | 3rd Octet | 4th octet | Host addresses
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| Class A | W | `255.0.0.0` | Network | Host | Host | Host | 16.7 million
| | `1` to `126` |
| Class B | W.X | `255.255.0.0`  | Network | Network | Host | Host | 65.5 thousand
| | `127` to `191`
| Class C | W.X.Y | `255.255.255.0` | Network | Network | Network | Host | 254
| | `192` to `223`
| Class D | `224` to `239` |
| Class E | `240` to `255`

## CIDR

- `255.255.255.0` == `/24` == `24` binary 1s continuously
- Masks must be contiguous - continuous 1s
- With CIDR, subnet mask does not have to be at the octet boundary
- Divide between host and network is not at the octet
- CIDR can implement variable subnet mask 
