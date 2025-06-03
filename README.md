# Network Scanner - Port Scanning Tool

A simple Python-based network scanner that performs TCP port scans on a target IP address. This tool mimics the basic behavior of popular tools like Nmap, providing insight into open ports on a machine within a specified range.

## Features

- **Simple TCP Port Scanning**: Uses socket connections to test port accessibility
- **Service Identification**: Maps common ports to well-known services (HTTP, SSH, FTP, etc.)
- **Flexible Port Range**: Scan any range of ports from 1 to 65535
- **Interactive Interface**: User-friendly command-line interface
- **Lightweight**: Uses only Python standard library (no external dependencies)
- **Cross-platform**: Works on Windows, macOS, and Linux

## Requirements

- Python 3.x
- No external dependencies (uses only standard library)

## Installation

1. Clone or download this repository
2. Ensure Python 3.x is installed on your system
3. Make the script executable (Linux/macOS):
   ```bash
   chmod +x network_scanner.py
   ```

## Usage

### Interactive Mode

Run the script directly for an interactive experience:

```bash
python3 network_scanner.py
```

The script will prompt you for:
- Target IP address
- Starting port number (default: 1)
- Ending port number (default: 1024)
- Timeout in seconds (default: 1)

### Programmatic Usage

You can also import and use the functions in your own scripts:

```python
from network_scanner import scan_ports

# Scan ports 20-1024 on localhost
target_ip = "127.0.0.1"
open_ports = scan_ports(target_ip, 20, 1024)
print(f"Found {len(open_ports)} open ports")
```

### Example Output

```
Network Scanner - Port Scanning Tool
====================================

==================================================
Network Scanner - Port Scan Results
==================================================
Target IP: 127.0.0.1
Port Range: 20 - 1024
Scan started at: 2024-01-15 14:30:25
==================================================
Port    22 - OPEN  [SSH]
Port    80 - OPEN  [HTTP]
Port   443 - OPEN  [HTTPS]

==================================================
Scan completed at: 2024-01-15 14:30:28
Total open ports found: 3
Open ports: 22, 80, 443
==================================================
```

## Functions

### `scan_port(target_ip, port, timeout=1)`
Scans a single port on the target IP address.

**Parameters:**
- `target_ip` (str): The IP address to scan
- `port` (int): The port number to scan
- `timeout` (int): Connection timeout in seconds (default: 1)

**Returns:**
- `bool`: True if port is open, False otherwise

### `scan_ports(target_ip, start_port, end_port, timeout=1)`
Scans a range of ports on the target IP address.

**Parameters:**
- `target_ip` (str): The IP address to scan
- `start_port` (int): Starting port number
- `end_port` (int): Ending port number
- `timeout` (int): Connection timeout in seconds (default: 1)

**Returns:**
- `list`: List of open ports

### `get_service_name(port)`
Returns the common service name for well-known ports.

**Parameters:**
- `port` (int): Port number

**Returns:**
- `str`: Service name if known, "Unknown" otherwise

## Supported Services

The scanner recognizes these common services:

| Port | Service |
|------|---------|
| 20   | FTP Data |
| 21   | FTP Control |
| 22   | SSH |
| 23   | Telnet |
| 25   | SMTP |
| 53   | DNS |
| 80   | HTTP |
| 110  | POP3 |
| 143  | IMAP |
| 443  | HTTPS |
| 993  | IMAPS |
| 995  | POP3S |

## Performance Notes

- **Timeout**: Lower timeout values (0.5-1 second) provide faster scans but may miss slower services
- **Range**: Scanning large port ranges (1-65535) can take significant time
- **Network**: Performance depends on network latency and target responsiveness

## Security and Legal Considerations

⚠️ **IMPORTANT LEGAL NOTICE** ⚠️

**Use this tool only on:**
- Your own machines and networks
- Systems where you have explicit written permission to perform security testing
- Test environments and lab setups

**Do NOT use this tool for:**
- Unauthorized scanning of networks or systems
- Penetration testing without proper authorization
- Any activity that violates local, state, or federal laws

Unauthorized port scanning may:
- Violate computer crime laws
- Breach network usage policies
- Trigger security alerts and incident responses
- Result in legal consequences

**Always ensure you have proper authorization before scanning any network or system.**

## Limitations

- **TCP Only**: This scanner only tests TCP connections, not UDP
- **No Stealth**: Uses direct socket connections (easily detectable)
- **No Threading**: Scans ports sequentially (single-threaded)
- **Basic Detection**: Only tests connectivity, doesn't perform banner grabbing

## Possible Extensions

Consider these enhancements for more advanced usage:

1. **Threading Support**: Implement multi-threading for faster scans
2. **UDP Scanning**: Add UDP port scanning capabilities
3. **Banner Grabbing**: Identify specific service versions
4. **Output Formats**: Export results to JSON, CSV, or XML
5. **Stealth Techniques**: Implement SYN scanning or other stealth methods
6. **Web Interface**: Create a web-based UI for easier usage
7. **Progress Indicators**: Add progress bars for long scans
8. **Host Discovery**: Add ping sweep functionality

## Troubleshooting

### Common Issues

1. **Permission Denied**: Some systems require elevated privileges for certain scans
2. **Firewall Blocking**: Host firewalls may block or slow down scans
3. **Network Timeouts**: Increase timeout value for slower networks
4. **False Negatives**: Some services may not respond to direct socket connections

### Tips

- Test on localhost (127.0.0.1) first to verify functionality
- Use smaller port ranges for initial testing
- Adjust timeout based on network conditions
- Check firewall settings if getting unexpected results

## License

This tool is provided for educational and authorized security testing purposes only.

## Author

Network Scanner Tool - A simple educational port scanner implementation.