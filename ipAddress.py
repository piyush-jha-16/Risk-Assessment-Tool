import ipaddress
import subprocess

def ping_scan(network):
    print(f"Scanning {network} ...")
    net = ipaddress.ip_network(network, strict=False)
    active_hosts = []
    for ip in net.hosts():
        result = subprocess.run(['ping', '-n', '1', '-w', '100', str(ip)], stdout=subprocess.PIPE)
        if "TTL=" in result.stdout.decode():
            active_hosts.append(str(ip))
    return active_hosts

if __name__ == "__main__":
    network = "10.103.133.0/24"
    devices = ping_scan(network)
    print("\nActive Devices:")
    for device in devices:
        print(device)
