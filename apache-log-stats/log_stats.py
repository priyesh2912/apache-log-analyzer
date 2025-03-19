import argparse
import re
from collections import Counter

# Regular expression for parsing Combined Log Format
LOG_PATTERN = re.compile(
    r'(?P<host>\S+) \S+ \S+ \[(?P<timestamp>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<resource>\S+) \S+" '
    r'(?P<status>\d{3}) (?P<bytes>\S+)'
)

def parse_log_line(line):
    """Parses a single log line and extracts relevant fields."""
    match = LOG_PATTERN.match(line)
    if not match:
        return None
    
    data = match.groupdict()
    data['status'] = int(data['status'])
    data['bytes'] = int(data['bytes']) if data['bytes'].isdigit() else 0
    return data

def process_log_file(file_path):
    """Reads log file and computes statistics."""
    total_requests = 0
    total_bytes = 0
    resource_counter = Counter()
    host_counter = Counter()
    status_counter = Counter()

    with open(file_path, 'r') as file:
        for line in file:
            parsed_data = parse_log_line(line)
            if parsed_data:
                total_requests += 1
                total_bytes += parsed_data['bytes']
                resource_counter[parsed_data['resource']] += 1
                host_counter[parsed_data['host']] += 1
                status_counter[parsed_data['status'] // 100] += 1  # 2xx, 3xx, etc.

    return {
        "total_requests": total_requests,
        "total_bytes": total_bytes,
        "most_requested": resource_counter.most_common(1),
        "top_host": host_counter.most_common(1),
        "status_distribution": {
            f"{k}xx": round((v / total_requests) * 100, 2) if total_requests else 0
            for k, v in status_counter.items()
        }
    }

def main():
    parser = argparse.ArgumentParser(description="Apache Log Analyzer")
    parser.add_argument("logfile", help="Path to the log file")
    args = parser.parse_args()

    stats = process_log_file(args.logfile)

    print(f"Total Requests: {stats['total_requests']}")
    print(f"Total Data Transferred: {stats['total_bytes']} bytes")
    
    if stats["most_requested"]:
        resource, count = stats["most_requested"][0]
        print(f"Most Requested Resource: {resource} ({count} requests)")

    if stats["top_host"]:
        host, count = stats["top_host"][0]
        print(f"Top Host: {host} ({count} requests)")

    print("Status Code Distribution:")
    for status, percentage in stats["status_distribution"].items():
        print(f"  {status}: {percentage}%")

if __name__ == "__main__":
    main()
