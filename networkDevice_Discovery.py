def discover_network_devices():
    """
    Discovers active devices on the local network by scanning IP range.
    
    Features:
    - Automatically detects local network range
    - Scans all IPs in subnet (1-254)
    - Attempts to resolve hostnames
    - Identifies active devices
    
    Returns:
    - List of tuples (ip_address, hostname) for found devices
    """
    print(Fore.CYAN + "\nDiscovering devices on local network...")
    
    devices = []
    # Get local IP and determine network range
    local_ip = socket.gethostbyname(socket.gethostname())
    network_prefix = ".".join(local_ip.split(".")[:3]) + "."
    
    loading_animation("Scanning network range")
    
    # Scan all IPs in the local network range
    for i in range(1, 255):
        ip = network_prefix + str(i)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((ip, 80))  # Test port 80
            if result == 0:
                try:
                    hostname = socket.gethostbyaddr(ip)[0]
                except:
                    hostname = "Unknown"
                devices.append((ip, hostname))
                print(Fore.GREEN + f"Device found: {ip} - {hostname}")
            sock.close()
        except:
            pass
    
    return devices