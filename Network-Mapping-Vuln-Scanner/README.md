# Network Mapping & Vulnerability Scanning Tool

## Overview
This project provides a local network scanning tool that can identify open ports, running services, and potential vulnerabilities on your local machine or devices within your local network. It uses Nmap and Python to perform security assessments and generate structured reports.

## Features
- Local network device discovery
- Port and service scanning
- Vulnerability matching for common services
- Report generation (CSV, PDF)

## Setup Instructions
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   sudo apt install nmap
   ```

## How to Run the Script
The project includes several scanning scripts in the `src` directory:

1. `vulnerability_scanner.py`: Main script for comprehensive vulnerability scanning
2. `scan_to_console.py`: Basic port scanning with console output
3. `scan_to_csv.py`: Port scanning with CSV report generation
4. `scan_with_services.py`: Port scanning with service detection

To run the main vulnerability scanner:
```bash
python src/vulnerability_scanner.py
```

You can modify the target in the script:
- For scanning your local machine: Use `localhost` or `127.0.0.1`
- For scanning devices on your local network: Use your local network range (e.g., `192.168.1.0/24`)

## Sample Outputs
- `scan_report.csv`: Contains IP, Port, Service, State, and Potential Vulnerability columns.
- `scan_report.pdf`: (Optional) PDF version of the report.

## Tool Limitations
- Only works on local networks or localhost
- Requires Nmap to be installed and accessible
- Basic vulnerability matching (dictionary-based)
- Cannot scan devices outside your local network

## Files Included
- Python scripts in `src/` directory:
  - `vulnerability_scanner.py` (main script)
  - `scan_to_console.py`
  - `scan_to_csv.py`
  - `scan_with_services.py`
- Sample reports
- `requirements.txt`

---

*For educational use only. Always have permission before scanning any network.* 
