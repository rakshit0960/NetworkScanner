#!/usr/bin/env python3
"""
Example usage of the Network Scanner tool.

This script demonstrates various ways to use the network scanner
for different scanning scenarios.
"""

from network_scanner import scan_ports, scan_port, validate_ip

def example_localhost_scan():
    """Example: Scan common ports on localhost."""
    print("Example 1: Scanning common ports on localhost")
    print("-" * 50)

    target_ip = "127.0.0.1"

    # Scan common service ports
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995]

    print(f"Scanning specific ports on {target_ip}...")
    open_ports = []

    for port in common_ports:
        if scan_port(target_ip, port):
            open_ports.append(port)
            print(f"Port {port} is OPEN")

    print(f"\nSummary: {len(open_ports)} open ports found")
    print()

def example_range_scan():
    """Example: Scan a range of ports."""
    print("Example 2: Scanning port range 20-100 on localhost")
    print("-" * 50)

    target_ip = "127.0.0.1"
    start_port = 20
    end_port = 100

    open_ports = scan_ports(target_ip, start_port, end_port)
    print()

def example_quick_scan():
    """Example: Quick scan with shorter timeout."""
    print("Example 3: Quick scan with 0.5 second timeout")
    print("-" * 50)

    target_ip = "127.0.0.1"

    # Quick scan of web-related ports
    web_ports = [80, 443, 8000, 8080, 8443, 9000]

    print(f"Quick scanning web ports on {target_ip}...")

    for port in web_ports:
        if scan_port(target_ip, port, timeout=0.5):
            print(f"Port {port} is OPEN")

    print()

def example_ip_validation():
    """Example: Demonstrate IP validation."""
    print("Example 4: IP Address Validation")
    print("-" * 50)

    test_ips = [
        "127.0.0.1",      # Valid
        "192.168.1.1",    # Valid
        "10.0.0.1",       # Valid
        "256.256.256.256", # Invalid
        "not.an.ip",      # Invalid
        "192.168.1",      # Invalid
    ]

    for ip in test_ips:
        is_valid = validate_ip(ip)
        status = "VALID" if is_valid else "INVALID"
        print(f"{ip:20} - {status}")

    print()

def example_custom_scan():
    """Example: Custom scan with user-defined parameters."""
    print("Example 5: Custom scan demonstration")
    print("-" * 50)

    # You can modify these parameters
    target_ip = "127.0.0.1"
    port_list = [22, 80, 443, 3000, 5000, 8000]
    timeout = 1

    print(f"Scanning custom port list: {port_list}")
    print(f"Target: {target_ip}, Timeout: {timeout}s")
    print()

    for port in port_list:
        result = scan_port(target_ip, port, timeout)
        status = "OPEN" if result else "CLOSED"
        print(f"Port {port:5d} - {status}")

    print()

def main():
    """Run all examples."""
    print("Network Scanner - Usage Examples")
    print("=" * 50)
    print("Note: These examples scan localhost (127.0.0.1)")
    print("Make sure you have permission to scan the target.")
    print()

    try:
        example_localhost_scan()
        example_range_scan()
        example_quick_scan()
        example_ip_validation()
        example_custom_scan()

        print("All examples completed!")

    except KeyboardInterrupt:
        print("\nExamples interrupted by user.")
    except Exception as e:
        print(f"Error running examples: {e}")

if __name__ == "__main__":
    main()