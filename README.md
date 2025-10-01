# Cybersecurity Risk Assessment Tool

A comprehensive Python-based cybersecurity scanning tool designed to perform network security assessments and vulnerability detection. This tool provides essential security scanning capabilities for network administrators and cybersecurity professionals.

## Features

- **Open Port Scanner** - Scan target systems for open network ports and identify running services
- **Network Device Discovery** - Discover active devices on your local network
- **Traceroute Analysis** - Perform network path analysis to identify routing hops
- **Firewall Status Checker** - Analyze firewall configurations and port filtering status
- **Vulnerability Assessment** - Basic security vulnerability detection and risk identification
- **Security Report Generator** - Comprehensive security assessment reporting

## Installation

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Dependencies

Install the required Python packages:

```bash
pip install colorama requests
```

### Operating System Support

- Windows 10/11
- Linux (Ubuntu, CentOS, Debian)
- macOS

## Usage

### Running the Tool

```bash
python cybersecurity_scanner.py
```

### Menu Options

1. **Scan for Open Ports**
   - Enter target IP address or hostname
   - Scans common ports (21, 22, 23, 80, 443, etc.)
   - Identifies services running on open ports
   - Provides detailed port status report

2. **Discover Network Devices**
   - Automatically scans local network range
   - Identifies active devices with IP addresses
   - Attempts hostname resolution
   - Provides device inventory list

3. **Perform Traceroute**
   - Enter target hostname or IP address
   - Cross-platform traceroute implementation
   - Shows network path and hops to destination
   - Helps diagnose network routing issues

4. **Check Firewall Status**
   - Tests target system for firewall protection
   - Analyzes port filtering behavior
   - Differentiates between closed and filtered ports
   - Provides firewall configuration assessment

5. **Vulnerability Assessment**
   - Basic security vulnerability scanning
   - Checks for common vulnerable services
   - Web server information disclosure analysis
   - Security recommendations and risk assessment

6. **Generate Security Report**
   - Comprehensive security assessment compilation
   - Professional report formatting
   - Timestamped scan results
   - Actionable security recommendations

## Code Structure

```
cybersecurity_scanner.py
├── print_header() - Displays tool header and clears screen
├── loading_animation() - Shows progress during operations
├── scan_open_ports() - Port scanning functionality
├── discover_network_devices() - Network device discovery
├── perform_traceroute() - Network path analysis
├── check_firewall_status() - Firewall configuration testing
├── vulnerability_assessment() - Security vulnerability scanning
├── generate_security_report() - Comprehensive reporting
└── main_menu() - User interface and menu system
```

## Example Usage

### Basic Port Scanning

```python
# Scan a specific target
target_ip = "192.168.1.1"
scan_open_ports(target_ip)

# Custom port range
ports = [22, 80, 443, 8080, 9000]
scan_open_ports(target_ip, ports)
```

### Network Discovery

```python
# Discover devices on local network
devices = discover_network_devices()
for ip, hostname in devices:
    print(f"Found: {ip} - {hostname}")
```

## Technical Details

### Port Scanning
- TCP Connect scanning method
- Configurable timeout settings
- Service name mapping for common ports
- Error handling for network issues

### Network Discovery
- Local network range detection
- Multi-threaded scanning approach
- Hostname resolution attempts
- Efficient timeout management

### Cross-Platform Support
- Windows: Uses `tracert` command
- Linux/macOS: Uses `traceroute` command
- Consistent output formatting
- Platform-specific optimizations

## Security Considerations

- This tool is designed for educational and authorized testing purposes only
- Always obtain proper authorization before scanning networks
- Some features may require administrative privileges
- Use responsibly and in compliance with local laws and regulations

## Troubleshooting

### Common Issues

1. **Permission Errors**
   - Run with administrative privileges for certain operations
   - Check firewall settings

2. **Network Timeouts**
   - Verify target accessibility
   - Check network connectivity
   - Adjust timeout settings in code

3. **Missing Dependencies**
   - Ensure all required packages are installed
   - Verify Python version compatibility

## Contributing

Contributions are welcome. Please ensure:

- Code follows PEP 8 style guidelines
- New features include proper documentation
- Tests are added for new functionality
- Security best practices are maintained

## License

This project is provided for educational purposes. Users are responsible for ensuring compliance with all applicable laws and regulations when using this tool.

## Disclaimer

This tool is intended for legitimate security assessment and educational purposes only. The developers are not responsible for any misuse or damage caused by this software. Always ensure you have proper authorization before conducting any security scans.

