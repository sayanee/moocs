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

## IP Subnetting

Calculate:

1. Subnet: `00000000`
1. 1st Host `00000001` == Subnet + 1
1. Last host: `11111110` == Broadcast - 1
1. Broadcast: `11111111` == Next network - 1

| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| ------ | ------ | ------| ------ | ------ | ------ | ------ | ------ |
| 128 | 192 | 224 | 240 | 248 | 252 | 254 | 255 |

- Hosts = 2^n - 2 (right to left)
- Networks = 2^n (left to right)

## Cabling and packet flows

- Communications
    - Unicast (1 to 1)
    - Broadcast (1 to many) - to all devices
    - Multicast (1 to some) - to only subscribed or opt-in devices
- OSI Model protocols
    - Layer 1: RJ-45, HUB
    - Layer 2: Bridge, Switch using MAC Address
    - Layer 3: Router using IP Address and MAC
    - Layer 4: TCP/UDP
- 10base2 Ethernet coaxial cable
    - baseband: single signal
    - broadband: multiple signal
- MAC Address
    - `48` bits
    - OUI: `24` bits from **Organizationally Unique Identifier (OUI)**
    - Station address: `24` bits from **Network Interface Controller (NIC)**
    - Check OUI list from [Wireshark](https://www.wireshark.org/tools/oui-lookup.html) or [IEEE](http://standards-oui.ieee.org/oui.txt)
- 10baseT
    - maximum segment is 100m.
    - shielded twisted pair used in noisy environment
    - **UTP: Unshielded Twisted Pair** - 4 twisted pair with an outer jacket

Cable categories

| Category | Frequency | Speed | Length
| ------ | ------ | ------ | ------ |
| `CAT5e` | `100MHz` | `1Gbps`
| `CAT6` | `250MHz` | `10Gbps` | `55m`
| `CAT6e` | `500MHz` | `10Gbps`| `100m`
| `CAT7` | `600MHz` | `10Gbps` | `100m`
| `CAT7a` | `1000MHz` | `100Gbps`
| `CAT8` | `40Gbps`

- **Hub (Layer 1) CAT5** - superseded by switches, multi-port repeater with no intelligence, physical star topology, logical bus topology
- **Switches (Layer 2)** - uses hardware to route traffic
- **Bride (Layer 2)** - maintains a list of MAC addresses learnt from the topology, uses ASIC that doesn't slow down the traffic, uses software to route traffic

| Bridge | Switch |
| ------ | ------ |
| Software | Hardware |
| Supports small number of ports | Support many ports |
| Replace switches today | Maintains a MAC address table

| Half Duplex | Full Duplex |
| ------- | ------ |
| Only 1 person can speak at a time | Both person can speak at the same time |

## TCP UDP

- no guarantee packets arrives
- packets might not be in order

| | Reliable | Best Effort / Unreliable
| ------ | ------ | ------ |
| Connection type | connection oriented | connectionless |
| Protocol | TCP | UDP
| Sequencing | Yes | No
| Application | HTTP, Email, FTP | Voice and video streaming

Common port numbers:

- `80` HTTP on TCP
- `21` FTP on TCP
- `23` Telnet on TCP
- `53` DNS on TCP/UDP

Port number ranges:

- Well-known ports `<=1023`
- Registered port `1024 - 49151`
- Dynamically assigned ports
    - IANA `49152 - 65535`
    - BSD `1024 - 4999`
    - Linux `32768 - 61000`

3-way TCP handshake:

1. Send `SYN`
1. Send `SYN, ACK`
1. Send `ACK`

## DHCP

1. Automatic allocation
    - assign a permanent IP address to a specific client based on E.g. MAC address
1. Dynamic Allocation
    - assign an IP for a period of time
    - IP address can be re-used
1. Manual Allocation
    - pre-allocate IP address to a device in the DHCP server

## VLANs

- same broadcast domain
- allows a logical network, not a physical network
- allows segmentation
- allows more flexible without changing physical cabling
- allows security with more segregated
- note physical topology vs logical topology

## Routing

- **Routed protocols**: IPv4, IPv6 carrying user data
- **Routing protocols**: EIGRP (bandwidth and delay), OSPF (bandwidth), RIP (hopcount), ISIS, BGP
- **Static routes**: Manual update E.g. home router to the ISP
- **Dynamic routes**: Uses a routing protocol
