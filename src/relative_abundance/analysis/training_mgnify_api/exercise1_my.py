#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import csv
import sys
from urllib.parse import urlencode

from jsonapi_client import Filter, Session

API_BASE = "https://www.ebi.ac.uk/metagenomics/api/v1"

# if you change the filters you may want to rename the output file
FILE_NAME = "exercise1_fecal.csv"

biome = "root:Host-associated:Human:Digestive system:Large intestine:Fecal"

print("Starting...")

with open(FILE_NAME, "w") as csvfile:
    # CSV initialization
    fieldnames = [
        "accession",
        "sample-name",
        "longitude",
        "latitude",
        "geo-loc-name",
        "studies",
        "biome",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # API call
    with Session(API_BASE) as session:

        # configure the filters
        params = {
            "experiment_type": "metagenomic",
            "ordering": "accession",
            # Exercise STEP
            # other filters should be placed here
        }

        api_filter = Filter(urlencode(params))
        print(api_filter.__str__())

        total = 0

        # sessions.iterate will take care of the pagination for us
        for sample in session.iterate(
            f"biomes/{biome}/samples", api_filter
        ):
            total += 1
            row = {
                "accession": sample.accession,
                "sample-name": sample.sample_name,
                "geo-loc-name": sample.geo_loc_name,
                "studies": ",".join([study.accession for study in sample.studies]),
                "biome": sample.biome.id,
            }
            writer.writerow(row)

        print("Data retrieved from the API")
