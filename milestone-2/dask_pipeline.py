from dask.distributed import Client
import time
import logging
from ingestion import ingest_logs
from parser import parse_log
from processing import process_logs

# ---------------- Logging ----------------
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def parse_batch(log_batch):
    results = []
    for log in log_batch:
        parsed = parse_log(log)
        if parsed:
            results.append(parsed)
    return results


def run_dask(file_path):
    client = Client()
    print("Dask cluster started:", client)
    print("Dask Dashboard Link:", client.dashboard_link)

    logging.info("Dask pipeline started")
    start = time.time()

    logs = ingest_logs(file_path)
    print("Total logs ingested:", len(logs))
    logging.info(f"Logs ingested: {len(logs)}")

    # -------- Batching --------
    batch_size = 500
    batches = [logs[i:i + batch_size] for i in range(0, len(logs), batch_size)]
    logging.info(f"Batches created: {len(batches)}")

    # -------- Distributed Execution --------
    futures = client.map(parse_batch, batches)
    results = client.gather(futures)

    parsed_logs = []
    for batch in results:
        parsed_logs.extend(batch)

    print("Sample processed logs:", parsed_logs[:3])
    logging.info(f"Parsed logs: {len(parsed_logs)}")

    # -------- Analytics --------
    error_count = process_logs(parsed_logs)

    end = time.time()
    total_time = end - start
    throughput = len(parsed_logs) / total_time if total_time > 0 else 0

    print("Dask Processing Time:", total_time)
    print("Throughput:", throughput, "logs/sec")

    logging.info(f"Processing Time: {total_time}")
    logging.info(f"Throughput: {throughput}")
    logging.info("Dask pipeline completed")
    input("Press Enter to close Dask client...")
    client.close()
    return parsed_logs


if __name__ == "__main__":
    run_dask("data/sample_logs.jsonl")