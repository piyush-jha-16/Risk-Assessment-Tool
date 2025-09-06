import socket
import time
from colorama import init, Fore, Style

def print_header():
    print(Fore.CYAN + "=" * 50)
    print(Fore.GREEN + Style.BRIGHT + "      CYBERSECURITY SYSTEM SCANNER")
    print(Fore.CYAN + "=" * 50)
    print()

# Open Port Scanner
def scan_open_ports(target_ip, ports=[21, 22, 23, 80, 443, 8080]):
    print(f"\nScanning {target_ip} for open ports...\n")
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  
        result = sock.connect_ex((target_ip, port))  
        if result == 0:
            print(f"Port {port} is OPEN")
            open_ports.append(port)
        else:
            print(f"Port {port} is CLOSED")
        sock.close()
    if open_ports:
        print(f"\nOpen Ports: {open_ports}")
    else:
        print("\nNo Open Ports Found.")
    input("\nPress Enter to return to menu...")

# Menu system
def main_menu():
    while True:
        print_header()
        print(Fore.BLUE + "[1] Scan for Open Ports")
        print(Fore.BLUE + "[8] Exit")
        print()

        choice = input(Fore.CYAN + "Select an option: ")

        if choice == '1':
            print(Fore.CYAN + "\nEnter target IP address or hostname (e.g., 192.168.1.1 or localhost): ")
            target_ip = input()
            scan_open_ports(target_ip)

        elif choice == '8':
            print(Fore.GREEN + "\nExiting... Thank you!")
            break

if __name__ == "__main__":
    main_menu()
