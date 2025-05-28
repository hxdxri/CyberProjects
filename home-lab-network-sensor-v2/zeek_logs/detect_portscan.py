import os
import datetime
from collections import defaultdict

# Path to Zeek conn.log
LOG_PATH = "../zeek_logs/conn.log"

# Time window (seconds) and threshold for port scans
TIME_WINDOW = 60
PORT_THRESHOLD = 100

def parse_conn_log(log_path):
    port_scan_candidates = defaultdict(list)

    with open(log_path, "r") as f:
        for line in f:
            if line.startswith("#"):
                continue  # skip headers and comments

            fields = line.strip().split('\t')
            if len(fields) < 5:
                continue

            ts, uid, orig_h, resp_h, resp_p = fields[:5]

            try:
                timestamp = datetime.datetime.utcfromtimestamp(float(ts))
                port = int(resp_p)
            except ValueError:
                continue

            port_scan_candidates[orig_h].append((timestamp, port))

    return port_scan_candidates

def detect_scans(candidates):
    print("🔍 Scanning for port scans...\n")
    for ip, entries in candidates.items():
        entries.sort()
        ports_seen = set()
        window_start = entries[0][0]

        for timestamp, port in entries:
            if (timestamp - window_start).seconds > TIME_WINDOW:
                if len(ports_seen) > PORT_THRESHOLD:
                    print(f"[⚠️ ALERT] Possible port scan from {ip}: {len(ports_seen)} ports in {TIME_WINDOW}s")
                # reset
                ports_seen = set()
                window_start = timestamp
            ports_seen.add(port)

if __name__ == "__main__":
    log_data = parse_conn_log(LOG_PATH)
    detect_scans(log_data)
