#!/usr/bin/env python3
"""
Network Scanner with Service Detection
Scans ports and identifies running services
"""

import subprocess
import csv
from datetime import datetime
import os

def run_scan(target: str) -> str:
    """Run Nmap scan with service detection on the target."""
    try:
        # Use -sV flag for service detection
        cmd = ['nmap', '-sV', target]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error scanning {target}: {str(e)}")
        return ""

def parse_scan_output(output: str) -> list:
    """Parse Nmap output to get open ports and their services."""
    ports_info = []
    for line in output.split('\n'):
        if '/tcp' in line and 'open' in line:
            # Parse the line to get port, service, and version
            parts = line.split()
            if len(parts) >= 4:
                port = parts[0].split('/')[0]
                state = parts[1]
                service = parts[2]
                # Version might be multiple words, join them
                version = ' '.join(parts[3:]) if len(parts) > 3 else 'unknown'
                
                ports_info.append({
                    'port': port,
                    'state': state,
                    'service': service,
                    'version': version
                })
    return ports_info

def save_to_csv(target: str, ports_info: list, output_file: str):
    """Save scan results to a CSV file."""
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Get current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Write to CSV
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(['IP Address', 'Port', 'State', 'Service', 'Version', 'Scan Time'])
        # Write data
        for port_info in ports_info:
            writer.writerow([
                target,
                port_info['port'],
                port_info['state'],
                port_info['service'],
                port_info['version'],
                timestamp
            ])

def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Network Scanner with Service Detection')
    parser.add_argument('--target', required=True, help='Target IP address')
    parser.add_argument('--output', default='reports/scan_results.csv',
                       help='Output CSV file path (default: reports/scan_results.csv)')
    
    args = parser.parse_args()
    
    print(f"Scanning {args.target} for open ports and services...")
    output = run_scan(args.target)
    ports_info = parse_scan_output(output)
    
    print(f"\nFound {len(ports_info)} open ports:")
    for port_info in ports_info:
        print(f"Port {port_info['port']}: {port_info['service']} ({port_info['version']})")
    
    # Save results to CSV
    save_to_csv(args.target, ports_info, args.output)
    print(f"\nResults saved to {args.output}")

if __name__ == "__main__":
    main() 