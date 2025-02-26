#!/usr/bin/env python3

import csv
import json
import sys

# Get file paths from command line arguments
json_file_path = sys.argv[1]
csv_file_path = sys.argv[2]

# Load the JSON file
with open(json_file_path, "r", encoding="utf-8") as f_json:
    jsondata = json.load(f_json)

# Open the CSV file in write mode (text mode) and create a CSV writer
with open(csv_file_path, "w", newline="", encoding="utf-8") as f_csv:
    writer = csv.writer(f_csv)
    # Write the CSV header
    writer.writerow([
                    # TODO: find a way to add the commented out columns
                    # "study-id",
                    # "sample-id",
                    "file-id",
                    "group",
                    "description",
                    "pipeline-verlink",
                    # "assembly/amplicon"
                   ])

    # Iterate over the entries in the "data" array
    for x in jsondata["data"]:
        writer.writerow(
            [
                # TODO: find a way to add the commented out columns
                # "study-id",
                # "sample-id",
                x["id"],
                x["attributes"]["group-type"],
                x["attributes"]["description"]["description"],
                x["relationships"]["pipeline"]["data"]["id"],
                x["links"]["self"],
                # "assembly/amplicon"
            ]
        )
