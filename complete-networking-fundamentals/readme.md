# Complete Networking Fundamentals

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
