# Linux Python Fundamentals Assignment - Cybersecurity Focus

## Assignment 1: Security Checker Scripts

### Script Overview
This repository contains three core security tools:

1. **ipChecker.py** - Validates IP address formats
2. **password_validor.py** - Checks password strength
3. **filePermissions.py** - Advanced security scanner (new)

### Security Checks Implemented

#### IP Address Validator (ipChecker.py)
- Verifies correct IPv4/IPv6 formatting
- Uses Python's built-in `ipaddress` module
- Provides clear feedback on invalid formats

#### Password Validator (password_validor.py)
- Enforces NIST-recommended policies:
  - 8+ characters
  - Upper/lowercase letters
  - Numbers and special characters

#### Advanced Security Scanner (filePermissions.py)
- **File Permission Checker**:
  - Identifies world-writable files (dangerous 777 permissions)
  - Recursively scans directories
  - Flags potential security risks

- **Log Analyzer**:
  - Counts security events (FAILED, ERROR, DENIED)
  - Case-insensitive pattern matching
  - Generates security reports

### Testing Methodology

#### IP Validator Tests
- Valid: `192.168.1.1`, `2001:db8::1`
- Invalid: `256.300.1.1`, `127.0.0.`

#### Password Validator Tests
- Weak: `password123`, `qwerty`
- Strong: `P@ssw0rd!Secure`

#### Security Scanner Tests
- World-writable files: `/tmp/testfile`
- Log analysis: `/var/log/auth.log`
- Tested with various permission scenarios

### Security Issues Found
1. Common world-writable files in /tmp
2. Excessive FAILED login attempts in logs
3. Weak password patterns
4. Malformed IP addresses in inputs

## Assignment 2: Cybersecurity Quiz Game

### Quiz Overview
The `QuizGame.py` script tests essential cybersecurity knowledge.

### Topics Covered
1. Password security
2. Phishing awareness
3. System hardening
4. Network security
5. Social engineering

## How to Run
```bash
# IP Validator
python3 ipChecker.py

# Password Validator
python3 password_validator.py

# Security Scanner
python3 security.py

# Security Quiz
python3 security_quiz.py
