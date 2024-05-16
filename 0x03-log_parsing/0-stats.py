#!/usr/bin/python3
import sys

# Custom function to calculate statistics
def calculate_stats(input_lines):
    # Initialize variables to store metrics
    total_file_size = 0
    status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    # Read input lines
    for line in input_lines:
        parts = line.split()
        # Check if the line matches the expected format
        if len(parts) == 7:
            try:
                file_size = int(parts[-1])
                status_code = int(parts[-2])
                total_file_size += file_size
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
                line_count += 1
                if line_count % 10 == 0:
                    print(f"Total file size: File size: {total_file_size}")
                    for code in sorted(status_code_counts.keys()):
                        print(f"{code}: {status_code_counts[code]}")
            except ValueError:
                pass
        if len(parts) != 7:
            continue

    # Print final statistics
    print(f"Total file size: File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")

# Entry point of the script
if __name__ == "__main__":
    try:
        input_lines = [line.strip() for line in sys.stdin]
        calculate_stats(input_lines)
    except KeyboardInterrupt:
        pass

