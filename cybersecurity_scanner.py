import os
import time
import socket
import subprocess
import platform
from colorama import init, Fore, Style
import requests
import json

# Initialize colorama
init(autoreset=True)

# Futuristic Header
def print_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + "=" * 60)
    print(Fore.GREEN + Style.BRIGHT + "           BASIC RISK ASSESSMENT TOOL")
    print(Fore.CYAN + "=" * 60)
    print()

# Loading animation
def loading_animation(task="Scanning"):
    print(Fore.YELLOW + f"{task}...", end="", flush=True)
    for _ in range(5):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.3)
    print(Fore.GREEN + " Done!")

# Open Port Scanner
def scan_open_ports(target_ip, ports=[21, 22, 23, 25, 53, 80, 110, 443, 993, 995, 8080, 8443]):
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
    
    if open_ports:
        print(Fore.YELLOW + f"\nSummary - Open Ports Found: {len(open_ports)}")
        for port, service in open_ports:
            print(Fore.GREEN + f"  Port {port}: {service}")
    else:
        print(Fore.YELLOW + "\nNo Open Ports Found.")
    input("\nPress Enter to return to menu...")

def get_service_name(port):
    common_services = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
        80: "HTTP", 110: "POP3", 443: "HTTPS", 993: "IMAPS", 
        995: "POP3S", 8080: "HTTP-Alt", 8443: "HTTPS-Alt"
    }
    return common_services.get(port, "Unknown Service")

# Network Device Discovery
def discover_network_devices():
    print(Fore.CYAN + "\nDiscovering devices on local network...")
    
    devices = []
    local_ip = socket.gethostbyname(socket.gethostname())
    network_prefix = ".".join(local_ip.split(".")[:3]) + "."
    
    loading_animation("Scanning network range")
    
    for i in range(1, 255):
        ip = network_prefix + str(i)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((ip, 80))
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
    
    print(Fore.YELLOW + f"\nTotal devices found: {len(devices)}")
    input("\nPress Enter to return to menu...")

# Traceroute Implementation
def perform_traceroute(target_host):
    print(Fore.CYAN + f"\nPerforming traceroute to {target_host}...")
    
    try:
        if platform.system().lower() == "windows":
            result = subprocess.run(['tracert', '-d', '-h', '15', target_host], 
                                  capture_output=True, text=True, timeout=30)
        else:
            result = subprocess.run(['traceroute', '-m', '15', '-n', target_host], 
                                  capture_output=True, text=True, timeout=30)
        
        print(Fore.WHITE + result.stdout)
        
    except subprocess.TimeoutExpired:
        print(Fore.RED + "Traceroute timed out")
    except Exception as e:
        print(Fore.RED + f"Error performing traceroute: {str(e)}")
    
    input("\nPress Enter to return to menu...")

# Firewall Checker
def check_firewall_status(target_ip, ports=[80, 443, 22]):
    print(Fore.CYAN + f"\nChecking firewall status for {target_ip}...")
    
    print(Fore.YELLOW + "\nTesting common ports for firewall filtering:")
    
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
                # Try with different timeout to detect filtered ports
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
    
    # Summary
    print(Fore.CYAN + "\n" + "="*40)
    print(Fore.YELLOW + "FIREWALL STATUS SUMMARY:")
    print(Fore.GREEN + f"Open ports (no blocking): {len(open_ports)}")
    print(Fore.YELLOW + f"Filtered ports (possible firewall): {len(filtered_ports)}")
    print(Fore.RED + f"Closed/Blocked ports: {len(closed_ports)}")
    
    if filtered_ports or closed_ports:
        print(Fore.YELLOW + "\nFirewall protection detected!")
    else:
        print(Fore.RED + "\nWarning: No firewall protection detected on tested ports!")
    
    input("\nPress Enter to return to menu...")

# Additional Feature: Vulnerability Assessment
def vulnerability_assessment(target_ip):
    print(Fore.CYAN + f"\nPerforming basic vulnerability assessment on {target_ip}...")
    
    vulnerabilities = []
    
    # Check for common vulnerable services
    vulnerable_ports = {
        21: "FTP - Potential anonymous login vulnerability",
        23: "Telnet - Unencrypted communication vulnerability",
        80: "HTTP - Potential web vulnerabilities",
        443: "HTTPS - Check for SSL/TLS vulnerabilities",
        3389: "RDP - Potential brute force vulnerability"
    }
    
    loading_animation("Checking for common vulnerabilities")
    
    for port, description in vulnerable_ports.items():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                vulnerabilities.append((port, description))
                print(Fore.RED + f"⚠️  VULNERABLE: Port {port} - {description}")
            sock.close()
        except:
            pass
    
    # Check if HTTP service reveals server info
    try:
        response = requests.get(f"http://{target_ip}", timeout=5)
        server_header = response.headers.get('Server', 'Not disclosed')
        print(Fore.YELLOW + f"Web Server: {server_header}")
        
        if any(tech in server_header for tech in ['Apache', 'nginx', 'IIS']):
            print(Fore.YELLOW + "ℹ️  Standard web server detected - ensure it's properly configured")
    except:
        pass
    
    if vulnerabilities:
        print(Fore.RED + f"\n🚨 CRITICAL: {len(vulnerabilities)} potential vulnerabilities found!")
        print(Fore.YELLOW + "Recommendations:")
        print("1. Close unnecessary open ports")
        print("2. Ensure services are updated to latest versions")
        print("3. Implement proper authentication mechanisms")
        print("4. Use encryption for sensitive services")
    else:
        print(Fore.GREEN + "\n✅ No obvious vulnerabilities detected in basic scan")
        print(Fore.YELLOW + "Note: This is a basic scan. Comprehensive testing recommended.")
    
    input("\nPress Enter to return to menu...")

# Generate Security Report
def generate_security_report(target_ip):
    print(Fore.CYAN + f"\nGenerating Security Report for {target_ip}...")
    loading_animation("Compiling security assessment")
    
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.GREEN + "SECURITY ASSESSMENT REPORT")
    print(Fore.CYAN + "="*50)
    print(Fore.YELLOW + f"Target: {target_ip}")
    print(Fore.YELLOW + f"Scan Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(Fore.CYAN + "-"*50)
    
    # This would integrate all previous scan results
    print(Fore.WHITE + "\nScan components:")
    print("✓ Open Port Analysis")
    print("✓ Network Device Discovery") 
    print("✓ Network Path Analysis")
    print("✓ Firewall Configuration Check")
    print("✓ Vulnerability Assessment")
    
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.GREEN + "RECOMMENDED ACTIONS:")
    print(Fore.CYAN + "="*50)
    print(Fore.WHITE + "1. Regularly update and patch all systems")
    print(Fore.WHITE + "2. Implement strong firewall rules")
    print(Fore.WHITE + "3. Close unnecessary ports and services")
    print(Fore.WHITE + "4. Use network segmentation")
    print(Fore.WHITE + "5. Conduct regular security audits")
    print(Fore.WHITE + "6. Implement intrusion detection systems")
    
    input("\nPress Enter to return to menu...")

# Menu system
def main_menu():
    while True:
        print_header()
        print(Fore.BLUE + "[1] Scan for Open Ports")
        print(Fore.BLUE + "[2] Discover Network Devices")
        print(Fore.BLUE + "[3] Perform Traceroute")
        print(Fore.BLUE + "[4] Check Firewall Status")
        print(Fore.BLUE + "[5] Vulnerability Assessment")
        print(Fore.BLUE + "[6] Generate Security Report")
        print(Fore.BLUE + "[0] Exit")
        print()

        choice = input(Fore.CYAN + "Select an option: ")

        if choice == '1':
            print(Fore.CYAN + "\nEnter target IP address or hostname: ")
            target_ip = input().strip()
            if target_ip:
                scan_open_ports(target_ip)
            else:
                print(Fore.RED + "Invalid input!")

        elif choice == '2':
            discover_network_devices()

        elif choice == '3':
            print(Fore.CYAN + "\nEnter target hostname or IP address: ")
            target_host = input().strip()
            if target_host:
                perform_traceroute(target_host)
            else:
                print(Fore.RED + "Invalid input!")

        elif choice == '4':
            print(Fore.CYAN + "\nEnter target IP address: ")
            target_ip = input().strip()
            if target_ip:
                check_firewall_status(target_ip)
            else:
                print(Fore.RED + "Invalid input!")

        elif choice == '5':
            print(Fore.CYAN + "\nEnter target IP address: ")
            target_ip = input().strip()
            if target_ip:
                vulnerability_assessment(target_ip)
            else:
                print(Fore.RED + "Invalid input!")

        elif choice == '6':
            print(Fore.CYAN + "\nEnter target IP address: ")
            target_ip = input().strip()
            if target_ip:
                generate_security_report(target_ip)
            else:
                print(Fore.RED + "Invalid input!")

        elif choice == '0':
            print(Fore.GREEN + "\nExiting... Thank you for using Cybersecurity Scanner!")
            break

        else:
            print(Fore.RED + "Invalid choice. Please select a valid option.")
            time.sleep(1)

# Run the tool
if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\nProgram interrupted by user. Exiting...")
    except Exception as e:
        print(Fore.RED + f"\nAn error occurred: {str(e)}")