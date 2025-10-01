def perform_traceroute(target_host):
    """
    Performs network path analysis to a target host.
    
    Features:
    - Cross-platform (Windows/Linux/macOS)
    - Shows network hops to destination
    - Identifies routing path
    - Helps diagnose network issues
    
    Parameters:
    - target_host: Destination hostname or IP address
    
    Returns:
    - Traceroute output as string
    """
    print(Fore.CYAN + f"\nPerforming traceroute to {target_host}...")
    
    try:
        # Platform-specific commands
        if platform.system().lower() == "windows":
            result = subprocess.run(['tracert', '-d', '-h', '15', target_host], 
                                  capture_output=True, text=True, timeout=30)
        else:
            result = subprocess.run(['traceroute', '-m', '15', '-n', target_host], 
                                  capture_output=True, text=True, timeout=30)
        
        print(Fore.WHITE + result.stdout)
        return result.stdout
        
    except subprocess.TimeoutExpired:
        print(Fore.RED + "Traceroute timed out")
        return "Timeout"
    except Exception as e:
        print(Fore.RED + f"Error performing traceroute: {str(e)}")
        return f"Error: {str(e)}"