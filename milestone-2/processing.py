def process_logs(parsed_logs):
    error_count = 0
    for log in parsed_logs:
        if log["level"] == "ERROR":
            error_count += 1

    print("Total ERROR logs:", error_count)
    return error_count