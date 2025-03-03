#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from urllib.parse import urlencode
from jsonapi_client import Filter, Session

API_BASE = "https://www.ebi.ac.uk/metagenomics/api/v1"
FILE_NAME = "./fetch_studies_assembly_op.csv"
biome = "root:Host-associated:Human:Digestive system:Large intestine:Fecal"
experiment_type = "assembly"

print("Starting...")

with open(FILE_NAME, "w", newline="") as csvfile:
    fieldnames = [
        "id", "sample-count", "bioproject", "secondary-accession",
        "study-abstract", "study-name", "samples"
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    with Session(API_BASE) as session:
        params = {
            "experiment_type": experiment_type,
            "lineage": biome,
        }
        api_filter = Filter(urlencode(params))  # Directly use dictionary instead of urlencode

        total = 0
        buffer = []  # Store rows before writing in batches

        for sample in session.iterate("studies", api_filter):
            total += 1
            if total % 100 == 0:  # Print progress every 100 records
                print(f"Processed {total} records...")

            row = {
                "id": sample.id,
                "sample-count": sample.samples_count,
                "bioproject": sample.bioproject,
                "secondary-accession": sample.secondary_accession,
                "study-abstract": sample.study_abstract,
                "study-name": sample.study_name,
                "samples": ",".join(study.accession for study in sample.samples),
            }
            buffer.append(row)

            if len(buffer) >= 500:  # Write in batches of 500
                writer.writerows(buffer)
                buffer.clear()

        # Write any remaining data
        if buffer:
            writer.writerows(buffer)

print(f"Data retrieval complete. Total records: {total}")
