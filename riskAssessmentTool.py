import os
import time
from colorama import init, Fore, Style
import socket


# Initialize colorama
init(autoreset=True)

# Futuristic Header
def print_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + "=" * 50)
    print(Fore.GREEN + Style.BRIGHT + "      CYBERSECURITY SYSTEM SCANNER")
    print(Fore.CYAN + "=" * 50)
    print()

# Loading animation
def loading_animation(task="Scanning"):
    print(Fore.YELLOW + f"{task}...", end="", flush=True)
    for _ in range(5):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.3)
    print(Fore.GREEN + " Done!")

#Open Port Scanner
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
        print(Fore.BLUE + "[0] Exit")
        print()

        choice = input(Fore.CYAN + "Select an option: ")

        if choice == '1':
            print(Fore.CYAN + "\nEnter target IP address or hostname (e.g., 192.168.1.1 or localhost): ")
            target_ip = input()
            scan_open_ports(target_ip)

        elif choice == '0':
            print(Fore.GREEN + "\nExiting... Thank you!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please select a valid option.")
            time.sleep(1)

# Run the tool
if __name__ == "__main__":
    main_menu()
