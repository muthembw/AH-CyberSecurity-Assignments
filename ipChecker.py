#!/usr/bin/env python3
# IP Address Validator
# Checks if user-input IP addresses are properly formatted

import ipaddress

def validate_ip(ip):
    """
    Validates whether a string is a properly formatted IPv4 or IPv6 address.
    Args:
        ip (str): The IP address to validate
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        ipaddress.ip_address(ip)  # Uses Python's built-in ipaddress module
        print(f"[✓] {ip} is a valid IP address.")
        return True
    except ValueError:
        print(f"[!] {ip} is not a valid IP address.")
        return False

# Main loop
while True:
    ip_address = input("\nEnter an IP address or type 'quit' to exit: ").strip()
    
    if ip_address.lower() == 'quit':
        print("Exiting IP validator...")
        break
    
    if not ip_address:
        print("[!] IP address cannot be empty.")
        continue
    
    validate_ip(ip_address)
