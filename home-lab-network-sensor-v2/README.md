#  Home Lab Network Sensor

A lightweight network activity monitor built with Python and Zeek to detect suspicious patterns (like IP spikes or port scans) in a home lab environment.

##  Features
- Parses Zeek `conn.log` files
- Flags high connection spikes from any IP
- Classifies alerts (Low / Medium / High threat)
- Prints real-time alerts to console
- Designed for simplicity and fast prototyping

##  Usage

1. Make sure Zeek is running and logging traffic.
2. Run the script:
   ```bash
   python3 monitor.py
