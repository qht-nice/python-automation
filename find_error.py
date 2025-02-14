#!/usr/bin/env python3
import sys
import os
import re

def error_search(log_file):
    error = input("What is the error? ").strip().lower()
    error_patterns = ["error"] + [re.escape(word) for word in error.split()]

    with open(log_file, encoding='UTF-8') as file:
        return [log for log in file if all(re.search(pattern, log.lower()) for pattern in error_patterns)]

def file_output(errors):
    error_log_path = os.path.expanduser('~/data/errors_found.log')
    os.makedirs(os.path.dirname(error_log_path), exist_ok=True)

    with open(error_log_path, 'w') as file:
        file.writelines(errors)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]

    if not os.path.isfile(log_file):
        print(f"Error: The file '{log_file}' does not exist.")
        sys.exit(1)

    errors = error_search(log_file)
    file_output(errors)
    print(f"Errors saved to {os.path.expanduser('~')}/data/errors_found.log")
    sys.exit(0)
