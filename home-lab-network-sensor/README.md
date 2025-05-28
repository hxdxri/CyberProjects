
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
=======
This is a modular, real-time network monitoring sensor designed for home lab environments. It captures, analyzes, and logs network traffic using tools like Zeek and Snort. It’s part of a broader cybersecurity project to detect anomalies, log flows, and trigger alerts in small-scale networks.

---

##  Objective

Build a reliable, hands-on sensor for home labs to:
- Detect anomalies (port scans, DNS spikes, MAC spoofing)
- Collect traffic logs for forensic analysis
- Trigger customizable alerts
- Serve as a base for future SIEM integration

---

##  Tools Used

- **Zeek** – Deep traffic analysis
- **Snort** – Intrusion detection via rule sets
- **tcpdump** – Packet capture
- **Python** – Alert parsing, scripting
- **Bash** – Automation and setup

---

##  Directory Structure

```bash
home-lab-network-sensor/
├── zeek-logs/                # Zeek log outputs
├── snort-config/             # Snort rules and configs
├── packet-captures/          # Captured traffic
├── scripts/
│   ├── alert-generator.py    # Alert logic
│   └── setup-monitor.sh      # Interface + tool bootstrap
├── requirements.txt          # Python deps
└── README.md                 
>>>>>>> 2deda4824554a724d6037a2724eaa77100f04a59
