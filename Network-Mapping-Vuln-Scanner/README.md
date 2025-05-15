# Network Mapping & Vulnerability Scanning Tool

## Overview
This project maps a network, scans devices for open ports and services, and identifies potential vulnerabilities using Nmap and Python. It generates structured reports and is designed for educational and practical cyber security use.

## Features
- Network topology mapping (with Cisco Packet Tracer)
- Automated port and service scanning (Python + Nmap)
- Vulnerability matching for common services
- Report generation (CSV, PDF)
- Optional integration with OpenVAS/Nessus

## Setup Instructions
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   sudo apt install nmap
   ```
3. (Optional) Set up Cisco Packet Tracer and export your .pkt file for reference.

## How to Run the Script
1. Edit `scan.py` to set your target subnet (default: `192.168.1.0/24`).
2. Run the scan:
   ```bash
   python scan.py
   ```
3. Reports will be generated in CSV and (optionally) PDF format.

## Sample Outputs
- `scan_report.csv`: Contains IP, Port, Service, State, and Potential Vulnerability columns.
- `scan_report.pdf`: (Optional) PDF version of the report.

## Tool Limitations
- Only basic vulnerability matching (dictionary-based)
- Requires Nmap to be installed and accessible
- Network topology design is manual (via Packet Tracer)
- OpenVAS/Nessus integration is optional and not automated

## Files Included
- `.pkt` file (network topology)
- Python scripts (`scan.py`, `vuln_services.py`, `report_gen.py`)
- Sample reports
- `requirements.txt`

---

*For educational use only. Always have permission before scanning any network.* 
