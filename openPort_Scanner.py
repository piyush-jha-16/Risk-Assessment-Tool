def scan_open_ports(target_ip, ports=[21, 22, 23, 25, 53, 80, 110, 443, 993, 995, 8080, 8443]):
    """
    Scans a target IP for open ports and identifies the services running on them.
    
    Features:
    - Tests common network ports
    - Identifies service names
    - Provides detailed port status
    - Returns list of open ports with services
    
    Parameters:
    - target_ip: IP address or hostname to scan
    - ports: List of ports to check (default common ports)
    
    Returns:
    - List of tuples (port, service_name) for open ports
    """
    print(f"\nScanning {target_ip} for open ports...\n")
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                service_name = get_service_name(port)
                print(Fore.GREEN + f"Port {port} is OPEN - {service_name}")
                open_ports.append((port, service_name))
            else:
                print(Fore.RED + f"Port {port} is CLOSED")
            sock.close()
        except Exception as e:
            print(Fore.RED + f"Error scanning port {port}: {str(e)}")
    
    return open_ports

def get_service_name(port):
    """
    Maps common port numbers to their service names.
    
    Parameters:
    - port: Port number
    
    Returns:
    - Service name as string
    """
    common_services = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
        80: "HTTP", 110: "POP3", 443: "HTTPS", 993: "IMAPS", 
        995: "POP3S", 8080: "HTTP-Alt", 8443: "HTTPS-Alt",
        143: "IMAP", 587: "SMTP-Submission", 993: "IMAPS",
        3306: "MySQL", 5432: "PostgreSQL", 27017: "MongoDB"
    }
    return common_services.get(port, "Unknown Service")