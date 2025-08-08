#!/usr/bin/env python3
# Password Strength Validator
# Checks if passwords meet minimum security requirements

import re

def validate_password(password):
    """
    Validates password against security criteria.
    Returns True if password meets all requirements, False otherwise.
    
    Criteria:
    - Not empty
    - Minimum 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    
    Args:
        password (str): The password to validate
        
    Returns:
        bool: Validation result
    """
    
    # Check for empty password
    if not password:
        print("[!] Error: Password cannot be empty.")
        return False
        
    # Check minimum length requirement
    if len(password) < 8:
        print("[!] Weak: Must be at least 8 characters")
        return False
        
    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        print("[!] Weak: Needs at least one uppercase letter (A-Z)")
        return False
        
    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        print("[!] Weak: Needs at least one lowercase letter (a-z)")
        return False
        
    # Check for at least one digit
    if not re.search(r"[0-9]", password):
        print("[!] Weak: Needs at least one number (0-9)")
        return False
        
    # Check for at least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("[!] Weak: Needs at least one special character (!@#$...)")
        return False
        
    # If all checks pass
    print("[✓] Strong: Password meets all security requirements")
    return True


def main():
    """Main program loop for password validation"""
    
    print("\n=== Password Validator ===")
    print("Requirements: 8+ chars, upper/lowercase, number, special character\n")
    
    while True:
        # Get password input (strip whitespace)
        password = input("Enter password (or 'quit' to exit): ").strip()
        
        # Exit condition
        if password.lower() == 'quit':
            print("Exiting validator...")
            break
            
        # Validate and break loop if valid
        if validate_password(password):
            print("Password accepted!")
            break


if __name__ == "__main__":
    main()
