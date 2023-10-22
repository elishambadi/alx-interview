#!/usr/bin/python3
"""Log parsing Module for python"""
import sys
import signal

status_code_counts = {}

total_file_size = 0
line_count = 0

def print_statistics(signal, frame):
    """Prints Log statistics when Ctrl+c signal is passed"""
    print("Total file size:", total_file_size)

    for status_code in sorted(status_code_counts.keys()):
        print(f"{status_code}: {status_code_counts[status_code]}")
    
    sys.exit(0)

signal.signal(signal.SIGINT, print_statistics)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) == 7:
            status_code = parts[5]
            try:
                file_size = int(parts[6])
            except ValueError:
                continue

            total_file_size += file_size
            
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1
            
            line_count += 1
            
            if line_count % 10 == 0:
                print("Total file size:", total_file_size)
                for status_code in sorted(status_code_counts.keys()):
                    print(f"{status_code}: {status_code_counts[status_code]}")

except KeyboardInterrupt:
    print_statistics(None, None)
