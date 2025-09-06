# Cybersecurity System Scanner  

A lightweight and easy-to-use **Cybersecurity Risk Assessment Tool** built in Python that helps detect and analyze potential vulnerabilities in a system and network. This tool is designed for students, researchers, and beginners in cybersecurity to understand how system risks can be identified with simple checks.  

---

## Features  
- **Open Port Scanner** → Scans common ports (21, 22, 23, 25, 80, 443, 8080) to check for open/closed ports.  
- **Connected Devices Scanner** → Lists all devices connected to the same Wi-Fi/network.  
- **Network Status Check** → Tests connectivity and latency (ping).  
- **System Uptime Monitor** → Displays how long the system has been running.  
- **Disk Space Monitor** → Shows available vs used disk space.  
- **Firewall Status Check** *(planned)* → Detect if firewall is enabled/disabled.  
- **Internet Speed Test** *(optional)* → Measures upload and download speeds.  

---

## Problem it Solves  
Many users are unaware of hidden risks such as **open ports, unauthorized devices, or misconfigured firewalls**.  
Existing solutions are often **complex, Linux-only, or require third-party installations**.  
This project provides a **simple yet effective tool** to quickly assess system and network security risks.  

---

## Tech Stack  
- **Python** (core language)  
- **socket** → For open port scanning  
- **subprocess** → For connected devices and system commands  
- **psutil** → For uptime and disk monitoring  
- **colorama** → For a user-friendly, futuristic CLI UI  

---

## Future Enhancements  
- Packet Sniffer (using `scapy`)  
- Intrusion Detection System (IDS)  
- Rootkit Detection  
- File Integrity Monitoring  
- Honeypot Simulation  

---

## Demo Screenshot  
*(Add screenshot of your tool’s menu here once it looks futuristic)*  

---

## Contribution  
Contributions are welcome! Fork this repo, add your feature, and create a PR.  
