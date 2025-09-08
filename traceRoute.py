import subprocess
import platform
import sys
def traceroute(target, max_hops=30):
    system = platform.system().lower()
    
    if system == "windows":
        cmd = ["tracert", "-d", "-h", str(max_hops), target]
    else:
        cmd = ["traceroute", "-n", "-m", str(max_hops), target]
    
    try:
        result = subprocess.check_output(cmd, text=True)
        print(result)
    except Exception as e:
        print(f"Error running traceroute: {e}")

if __name__ == "__main__":
    target = input("Enter target hostname or IP address: ")
    traceroute(target)