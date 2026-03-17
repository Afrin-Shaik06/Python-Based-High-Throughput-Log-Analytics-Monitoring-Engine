import json
import random
from datetime import datetime

levels = ["INFO", "WARN", "ERROR"]
services = ["auth-service", "payment-service", "order-service"]

with open("data/sample_logs.json", "w") as f:
    for i in range(5000):
        log = {
            "timestamp": datetime.now().isoformat(),
            "level": random.choice(levels),
            "service": random.choice(services),
            "message": f"Log message number {i}",
            "ip": f"192.168.1.{i % 255}"
        }
        f.write(json.dumps(log) + "\n")  # 🔥 Important: one JSON per line

print("5000 JSON-line logs generated.")
