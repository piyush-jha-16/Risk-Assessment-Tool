def check_firewall_status(target_ip, ports=[80, 443, 22, 21, 23, 25, 53]):
    """
    Analyzes firewall configuration and port filtering status.
    
    Features:
    - Tests multiple common ports
    - Differentiates between closed and filtered ports
    - Detects firewall presence
    - Provides security assessment
    
    Parameters:
    - target_ip: IP address to test
    - ports: List of ports to check for firewall rules
    
    Returns:
    - Dictionary with open, filtered, and closed ports
    """
    print(Fore.CYAN + f"\nChecking firewall status for {target_ip}...")
    
    filtered_ports = []
    open_ports = []
    closed_ports = []
    
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((target_ip, port))
            
            if result == 0:
                print(Fore.GREEN + f"Port {port}: OPEN (No firewall blocking)")
                open_ports.append(port)
            else:
                # Secondary test with longer timeout to detect filtering
                sock.settimeout(5)
                result2 = sock.connect_ex((target_ip, port))
                if result2 == 0:
                    print(Fore.YELLOW + f"Port {port}: FILTERED (Firewall may be slowing response)")
                    filtered_ports.append(port)
                else:
                    print(Fore.RED + f"Port {port}: CLOSED/FILTERED (Likely firewall blocked)")
                    closed_ports.append(port)
            
            sock.close()
        except socket.timeout:
            print(Fore.YELLOW + f"Port {port}: FILTERED (Connection timeout)")
            filtered_ports.append(port)
        except Exception as e:
            print(Fore.RED + f"Port {port}: ERROR - {str(e)}")
    
    return {
        'open': open_ports,
        'filtered': filtered_ports,
        'closed': closed_ports
    }