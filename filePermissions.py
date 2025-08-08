#!/usr/bin/env python3
# Security Scanner Script
# Performs two cybersecurity checks:
# 1. Finds world-writable files (dangerous permissions)
# 2. Analyzes log files for security events

import os
import stat
import re
from datetime import datetime

def check_world_writable_files(directory='.'):
    """
    Scans directory for world-writable files (dangerous permission)
    Args:
        directory (str): Path to scan (defaults to current directory)
    Returns:
        list: Paths of world-writable files
    """
    dangerous_files = []
    
    print(f"\n[🔍] Scanning {directory} for world-writable files...")
    
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                mode = os.stat(filepath).st_mode
                if mode & stat.S_IWOTH:  # Check world-writable bit
                    dangerous_files.append(filepath)
                    print(f"[⚠️] Dangerous permission: {filepath}")
            except Exception as e:
                print(f"[!] Error checking {filepath}: {str(e)}")
    
    return dangerous_files

def analyze_log_file(logfile, patterns=['FAILED', 'ERROR', 'DENIED']):
    """
    Counts security-relevant patterns in log files
    Args:
        logfile (str): Path to log file
        patterns (list): Security terms to search for
    Returns:
        dict: Counts of each pattern found
    """
    counts = {pattern: 0 for pattern in patterns}
    
    print(f"\n[📄] Analyzing {logfile} for security events...")
    
    try:
        with open(logfile, 'r') as f:
            for line in f:
                for pattern in patterns:
                    if re.search(pattern, line, re.IGNORECASE):
                        counts[pattern] += 1
                        
        for pattern, count in counts.items():
            print(f"[🔎] Found {count} occurrences of: {pattern}")
            
    except FileNotFoundError:
        print(f"[!] Error: Log file {logfile} not found")
    except Exception as e:
        print(f"[!] Error analyzing log: {str(e)}")
    
    return counts

def generate_report(findings, filename='security_report.txt'):
    """Generates a security report file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, 'a') as f:
        f.write(f"\n=== Security Scan Report ({timestamp}) ===\n")
        f.write("World-writable files found:\n")
        f.writelines(f"- {file}\n" for file in findings['world_writable'])
        f.write("\nSecurity events in logs:\n")
        for pattern, count in findings['log_counts'].items():
            f.write(f"- {pattern}: {count} occurrences\n")
    print(f"[✓] Report saved to {filename}")

def main():
    print("\n=== Security Scanner ===")
    print(f"Started at: {datetime.now()}\n")
    
    # Get user input
    scan_dir = input("Enter directory to scan (press Enter for current dir): ") or '.'
    log_file = input("Enter log file path to analyze: ")
    
    # Run security checks
    findings = {
        'world_writable': check_world_writable_files(scan_dir),
        'log_counts': analyze_log_file(log_file)
    }
    
    # Generate report
    generate_report(findings)
    
    print("\n[✅] Security scan completed")

if __name__ == "__main__":
    main()
