#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from urllib.parse import urlencode

from jsonapi_client import Filter, Session

API_BASE = "https://www.ebi.ac.uk/metagenomics/api/v1"
FILE_NAME = "./fetch_studies_assembly.csv"
biome = "root:Host-associated:Human:Reproductive system:Vagina"
experiment_type = "assembly"

print("Starting...")

with open(FILE_NAME, "w") as csvfile:
    # CSV initialization
    fieldnames = [
        "id",
        "sample-count",
        "bioproject",
        "secondary-accession",
        "study-abstract",
        "study-name",
        "samples",
        # "downloads",
        # "analyses",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # API call
    with Session(API_BASE) as session:
        # configure the filters
        params = {
            # 'accession': '',
            "experiment_type": experiment_type,
            # 'biome_name': '',
            "lineage": biome,
            # 'geo_loc_name': '',
            # 'latitude_gte': '',
            # 'latitude_lte': '',
            # 'longitude_gte': '',
            # 'longitude_lte': '',
            # 'species': '',
            # 'instrument_model': '',
            # 'instrument_platform': '',
            # 'metadata_key': '',
            # 'metadata_value_gte': '',
            # 'metadata_value_lte': '',
            # 'metadata_value': '',
            # 'environment_material': '',
            # 'environment_feature': '',
            # 'study_accession': '',
            # 'include': '',
            # 'format': 'csv'
        }

        api_filter = Filter(urlencode(params))

        total = 0

        # sessions.iterate will take care of the pagination for us
        for sample in session.iterate("studies", api_filter):
            total += 1
            print(f"page: {total} ...")
            rows = {
                "id": sample.id,
                "sample-count": sample.samples_count,
                "bioproject": sample.bioproject,
                "secondary-accession": sample.secondary_accession,
                "study-abstract": sample.study_abstract,
                "study-name": sample.study_name,
                "samples": ",".join([study.accession for study in sample.samples]),
                # "downloads": sample.downloads,
                # "analyses": sample.analyses,
            }
            writer.writerow(rows)

        print("Data retrieved from the API")
