# Linux Python Fundamentals Assignment - Cybersecurity Focus

## Assignment 1: Security Checker Script

### Script Overview
This repository contains two Python scripts that implement fundamental cybersecurity checks:

1. **ipChecker.py** - Validates IP address formats (both IPv4 and IPv6)
2. **password_validator.py** - Checks password strength against multiple criteria

### Security Checks Implemented
#### IP Address Validator
- Verifies correct IPv4/IPv6 formatting
- Uses Python's built-in `ipaddress` module for robust validation
- Provides clear feedback on invalid formats

#### Password Validator
- Enforces NIST-recommended password policies:
  - Minimum 8 characters length
  - Requires uppercase and lowercase letters
  - Requires at least one digit
  - Requires at least one special character
- Uses regular expressions for pattern matching

### Testing Methodology
#### IP Validator Tests
- Valid IPs: `192.168.1.1`, `0.0.0.0`, `2001:db8::1`
- Invalid IPs: `256.300.1.1`, `127.0.0.`, `2222/4r5.23.45`

#### Password Validator Tests
- Weak passwords: `password`, `12345678`, `Password`
- Strong password: `Secur3P@ss!2023`

### Security Issues Found
1. Many users attempt invalid IP formats
2. Common password weaknesses observed:
   - Missing special characters
   - All-lowercase letters
   - Insufficient length

## Assignment 2: Cybersecurity Quiz Game

### Quiz Overview
The `security_quiz.py` script tests knowledge of essential cybersecurity concepts through multiple-choice questions.

### Topics Covered
1. Password security best practices
2. Phishing attack identification
3. Importance of software updates
4. Secure Wi-Fi practices
5. Social engineering awareness

### Features
- Tracks correct/wrong answers
- Provides immediate feedback
- Offers security tips for incorrect answers
- Runs until user quits

### Testing Results
- Tested with various answer combinations
- Achieved perfect score with all correct answers
- Verified helpful tips appear for wrong answers

### Key Learnings
- Reinforced understanding of password complexity
- Highlighted importance of regular software updates
- Demonstrated common social engineering tactics

## How to Run
```bash
# IP Validator
python3 ipChecker.py

# Password Validator
python3 password_validator.py

# Security Quiz
python3 security_quiz.py
