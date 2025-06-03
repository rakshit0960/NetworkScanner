#!/usr/bin/env python3
"""
Network Scanner - Port Scanning Tool
====================================

A simple Python-based network scanner that performs TCP port scans on a target IP address.
This mimics the basic behavior of popular tools like Nmap, providing insight into open ports
on a machine within a specified range.

Features
--------
- Input target IP and port range
- TCP port scanning using socket connections
- Displays open ports to the user
- Optional: Map common ports to known services (e.g., HTTP, FTP)

Usage
-----
1. Set the target IP address (e.g., '127.0.0.1').
2. Specify the port range (e.g., 20–1024).
3. Call the `scan_ports` function.

Example::

    target_ip = "127.0.0.1"
    scan_ports(target_ip, 20, 1024)

Dependencies
------------
- Python 3.x
- Standard library only (socket)

Legal Notice
------------
Use this tool only on machines you own or have explicit permission to scan.
Unauthorized scanning may violate laws or network policies.

Author
------
Network Scanner Tool
"""

import socket
import sys
from datetime import datetime

# Common service mappings for well-known ports
COMMON_PORTS = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    993: "IMAPS",
    995: "POP3S"
}

def scan_port(target_ip, port, timeout=1):
    """
    Scan a single port on the target IP address.

    Args:
        target_ip (str): The IP address to scan
        port (int): The port number to scan
        timeout (int): Connection timeout in seconds

    Returns:
        bool: True if port is open, False otherwise
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        # Attempt to connect to the target IP and port
        result = sock.connect_ex((target_ip, port))
        sock.close()

        # If connection successful, port is open
        return result == 0
    except socket.gaierror:
        # Hostname could not be resolved
        return False
    except Exception:
        # Any other exception means port is closed
        return False

def get_service_name(port):
    """
    Get the common service name for a given port.

    Args:
        port (int): Port number

    Returns:
        str: Service name if known, "Unknown" otherwise
    """
    return COMMON_PORTS.get(port, "Unknown")

def scan_ports(target_ip, start_port, end_port, timeout=1):
    """
    Scan a range of ports on the target IP address.

    Args:
        target_ip (str): The IP address to scan
        start_port (int): Starting port number
        end_port (int): Ending port number
        timeout (int): Connection timeout in seconds

    Returns:
        list: List of open ports
    """
    open_ports = []

    print(f"\n{'='*50}")
    print(f"Network Scanner - Port Scan Results")
    print(f"{'='*50}")
    print(f"Target IP: {target_ip}")
    print(f"Port Range: {start_port} - {end_port}")
    print(f"Scan started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}")

    # Validate port range
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Error: Invalid port range. Ports must be between 1-65535 and start_port <= end_port")
        return open_ports

    # Scan each port in the specified range
    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port, timeout):
            service = get_service_name(port)
            open_ports.append(port)
            print(f"Port {port:5d} - OPEN  [{service}]")
        else:
            # Uncomment the line below to see closed ports as well
            # print(f"Port {port:5d} - CLOSED")
            pass

    print(f"\n{'='*50}")
    print(f"Scan completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total open ports found: {len(open_ports)}")

    if open_ports:
        print(f"Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found in the specified range.")

    print(f"{'='*50}\n")

    return open_ports

def validate_ip(ip_address):
    """
    Validate if the given string is a valid IP address.

    Args:
        ip_address (str): IP address to validate

    Returns:
        bool: True if valid IP, False otherwise
    """
    try:
        socket.inet_aton(ip_address)
        return True
    except socket.error:
        return False

def main():
    """
    Main function to run the network scanner interactively.
    """
    print("Network Scanner - Port Scanning Tool")
    print("====================================")
    print("Legal Notice: Use only on machines you own or have permission to scan.\n")

    try:
        # Get target IP from user
        target_ip = input("Enter target IP address (e.g., 127.0.0.1): ").strip()

        if not validate_ip(target_ip):
            print("Error: Invalid IP address format.")
            sys.exit(1)

        # Get port range from user
        start_port = int(input("Enter starting port (default: 1): ") or "1")
        end_port = int(input("Enter ending port (default: 1024): ") or "1024")

        # Optional: Get timeout value
        timeout_input = input("Enter timeout in seconds (default: 1): ").strip()
        timeout = int(timeout_input) if timeout_input else 1

        # Perform the scan
        open_ports = scan_ports(target_ip, start_port, end_port, timeout)

    except KeyboardInterrupt:
        print("\n\nScan interrupted by user.")
        sys.exit(0)
    except ValueError:
        print("Error: Please enter valid numeric values for ports and timeout.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()