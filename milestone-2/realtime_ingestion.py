import time
import glob
import os
from dask_pipeline import run_dask

processed_files = set()

def watch_directory():

    while True:
        files = glob.glob("data/*.json")

        new_files = [f for f in files if f not in processed_files]

        for file in new_files:
            print(f"Processing new file: {file}")
            run_dask(file)
            processed_files.add(file)

        time.sleep(5)  # check every 5 seconds

if __name__ == "__main__":
    watch_directory()