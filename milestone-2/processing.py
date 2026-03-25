import json
import pandas as pd

input_file = "data/sample_logs.json"
output_file = "processed_logs/output.csv"


def process_logs():

    logs = []

    with open(input_file, "r") as f:
        for line in f:
            log = json.loads(line)

            level = log["level"]

            # Simple anomaly rule
            anomaly = 1 if level == "ERROR" else 0

            logs.append({
                "@timestamp": log["timestamp"],
                "level": level,
                "service": log["service"],
                "message": log["message"],
                "anomaly": anomaly
            })

    df = pd.DataFrame(logs)

    error_count = df[df["level"] == "ERROR"].shape[0]

    print("Total ERROR logs:", error_count)

    df.to_csv(output_file, index=False)

    print("Processed logs saved to:", output_file)


if __name__ == "__main__":
    process_logs()