#!/usr/bin/env python3
"""
Simple Network Scanner
Basic port scanning with console output
"""

import subprocess

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

def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Simple Network Scanner')
    parser.add_argument('--target', required=True, help='Target IP address')
    
    args = parser.parse_args()
    
    print(f"Scanning {args.target}...")
    output = run_scan(args.target)
    ports = parse_scan_output(output)
    
    print(f"\nFound {len(ports)} open ports:")
    for port in ports:
        print(f"Port {port} is open")

if __name__ == "__main__":
    main() 