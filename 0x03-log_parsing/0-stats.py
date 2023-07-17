#!/usr/bin/python3
import sys
import re
from collections import defaultdict
"""
    Module to parse logs
"""


def compute_metrics():
    """
        Parses log output in a loop
        Args: stdin
        Returns: no. of log lines & status code counts
    """
    total_file_size = 0
    status_code_counts = defaultdict(int)

    try:
        line_count = 0

        for line in sys.stdin:
            line = line.strip()

            # Extract relevant information using regular expressions
            mc = re.match(r'^.*?"GET \/projects\/260.*?" (\d+) (\d+)$', line)
            if mc:
                status_code = match.group(1)
                file_size = int(match.group(2))

                # Update total file size
                total_file_size += file_size

                # Update status code counts
                if status_code.isdigit():
                    status_code_counts[status_code] += 1

                line_count += 1

                # Print statistics every 10 lines
                if line_count % 10 == 0:
                    print("File size:", total_file_size)
                    for code in sorted(status_code_counts.keys()):
                        print(code + ":", status_code_counts[code])

    except KeyboardInterrupt:
        pass

    print("File size:", total_file_size)
    for code in sorted(status_code_counts.keys()):
        print(code + ":", status_code_counts[code])


compute_metrics()
