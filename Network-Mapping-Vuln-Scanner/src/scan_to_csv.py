#!/usr/bin/env python3
"""
Network Scanner with CSV Output
Extends the basic scanner to save results to CSV files
"""

import subprocess
import csv
from datetime import datetime
import os

def run_scan(target: str) -> str:
    """Run a basic Nmap scan on the target."""
    try:
        # Basic scan with just port detection
        cmd = ['nmap', '-p-', target]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error scanning {target}: {str(e)}")
        return ""

def parse_scan_output(output: str) -> list:
    """Parse Nmap output to get open ports."""
    ports = []
    for line in output.split('\n'):
        if '/tcp' in line and 'open' in line:
            # Extract port number
            port = line.split('/')[0]
            ports.append(port)
    return ports

def save_to_csv(target: str, ports: list, output_file: str):
    """Save scan results to a CSV file."""
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Get current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Write to CSV
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(['IP Address', 'Port', 'Scan Time'])
        # Write data
        for port in ports:
            writer.writerow([target, port, timestamp])

def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Network Scanner with CSV Output')
    parser.add_argument('--target', required=True, help='Target IP address')
    parser.add_argument('--output', default='reports/scan_results.csv',
                       help='Output CSV file path (default: reports/scan_results.csv)')
    
    args = parser.parse_args()
    
    print(f"Scanning {args.target}...")
    output = run_scan(args.target)
    ports = parse_scan_output(output)
    
    print(f"\nFound {len(ports)} open ports:")
    for port in ports:
        print(f"Port {port} is open")
    
    # Save results to CSV
    save_to_csv(args.target, ports, args.output)
    print(f"\nResults saved to {args.output}")

if __name__ == "__main__":
    main() 