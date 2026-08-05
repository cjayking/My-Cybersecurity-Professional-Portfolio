# 3-Tier Enterprise DMZ Architecture & Perimeter Defense Lab

**Project:** Network Segmentation & Perimeter Defense using OPNsense

## Project Overview
This lab demonstrates the design and implementation of a secure 3-tier network architecture using OPNsense firewall. The goal is to isolate public-facing web infrastructure from internal administrative networks to prevent lateral movement in the event of a compromise.

## Objective
- Isolate public-facing services (Web Server) in a DMZ
- Protect internal (LAN) resources from direct external access
- Enforce strong perimeter security controls and TLS encryption

## Network Architecture
```text
                   +-------------------+
                   |   WAN (Internet)  |
                   +--------+----------+
                            |
                   [ OPNsense Firewall ]
                  /                   \
        +--------+--------+   +--------+---------+
        |   DMZ Subnet    |   |    LAN Subnet    |
        |(172.16.10.50/24)|   |(192.168.1.186/24)|
        +--------+--------+   +--------+---------+
                 |                     |
        [ Nginx Web Server]   [ Internal Admin ]
```
## Key Implementation Steps

### 1. Network Segmentation
- Created three virtual networks: WAN, LAN, and DMZ
- Configured OPNsense as the central firewall/router between all zones

### 2. Stateful Firewall Policy Design
- Applied **Implicit Deny** by default
- Created rules blocking DMZ → LAN traffic
- Allowed only necessary inbound traffic (HTTP/HTTPS) to the DMZ

### 3. Destination NAT (DNAT)
- Configured DNAT rules to forward external HTTP (80) and HTTPS (443) traffic to the Nginx web server in the DMZ

### 4. Web Server Hardening
- Deployed Nginx with custom RSA-2048 PKI certificates
- Enforced **TLS 1.3** only
- Restricted cipher suites to strong options (`TLS_AES_256_GCM_SHA384`)

## Validation & Security Telemetry

**TLS 1.3 Handshake Verification**  
![OpenSSL Handshake](./images/openssl-tls13.png)  
Verified using `openssl s_client` that only TLS 1.3 is accepted.

**Attack Surface Minimization**  
![Nmap Scan](./images/nmap-scan.png)  
`nmap -Pn -sV` confirms only ports 80 and 443 are open.

**Firewall Log Evidence**  
![OPNsense Drop Log](./images/opnsense-drop-log.png)  
OPNsense successfully drops unauthorized DMZ → LAN traffic.

## Key Skills Demonstrated
- Network segmentation & DMZ design
- Stateful firewall policy creation
- Destination NAT configuration
- TLS 1.3 enforcement & certificate management
- Security validation using OpenSSL and Nmap

## Tools Used
- OPNsense Firewall
- Nginx
- OpenSSL
- Nmap
- Virtualization (Proxmox / VMware / VirtualBox)
