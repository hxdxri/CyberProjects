import os
import time
import requests
from collections import defaultdict

LOG_PATH = "../zeek_logs/conn.log"
ALERT_THRESHOLD = 10
WEBHOOK_URL = "https://discord.com/api/webhooks/1376475711124017263/5sFM97jREulG9H9APr15sI8cQ9tUfCiFZkicAUGj0MHGzNFbUB8kIipnfa80wGdaBESb"

def send_alert(ip, count):
    message = f"🚨 Suspicious activity detected!\nIP `{ip}` has made `{count}` connections."
    payload = {"content": message}
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code != 204:
            print(f"[!] Failed to send alert: {response.status_code}")
    except Exception as e:
        print(f"[!] Error sending alert: {e}")

def parse_conn_log(path):
    conn_count = defaultdict(int)
    with open(path, 'r') as f:
        for line in f:
            if line.startswith("#") or line.strip() == "":
                continue
            fields = line.strip().split('\t')
            if len(fields) < 5:
                continue
            src_ip = fields[2]
            conn_count[src_ip] += 1

    for ip, count in conn_count.items():
        if count > ALERT_THRESHOLD:
            send_alert(ip, count)

if __name__ == "__main__":
    print("🔁 Starting real-time log monitoring...")
    while True:
        if os.path.exists(LOG_PATH):
            parse_conn_log(LOG_PATH)
        else:
            print(f"[!] Log not found: {LOG_PATH}")
        time.sleep(10)

