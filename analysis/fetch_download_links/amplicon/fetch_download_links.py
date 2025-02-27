#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from urllib.parse import urlencode
import pandas as pd

from jsonapi_client import Filter, Session

API_BASE = "https://www.ebi.ac.uk/metagenomics/api/v1"
FILE_NAME = "./fetch_download_links.csv"
csv_file = "./analysis/fetch_studies_amplicon.csv"

def fetch_download_links(ids:list):

    with open(FILE_NAME, "w") as csvfile:
        # CSV initialization
        fieldnames = [
            'study-id',
            'file-id',
            'type',
            'links.self',
            'meta',
            'pipelines',
            'alias',
            'file-format.name',
            'file-format.extension',
            'description.label',
            'description.description',
            'group-type',
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # API call
        with Session(API_BASE) as session:
            # configure the filters
            params = {
                # 'accession': '',
                # "experiment_type": experiment_type,
                # 'biome_name': '',
                # "lineage": biome,
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

            for id in ids:
                # sessions.iterate will take care of the pagination for us
                for sample in session.iterate(f"studies/{id}/downloads", api_filter):
                    total += 1
                    print(f"page: {total} ...")
                    rows = {
                        'study-id': id,
                        'file-id': sample.id,
                        'type': sample.type,
                        'links.self': sample.links.self,
                        'meta': sample.meta,
                        'pipelines': sample.pipeline,
                        'alias': sample.alias,
                        'file-format.name': sample.file_format.name,
                        'file-format.extension': sample.file_format.extension,
                        'description.label': sample.description.label,
                        'description.description': sample.description.description,
                        'group-type': sample.group_type,
                    }
                    writer.writerow(rows)

            print("Data retrieved from the API")


def main():
    print("Starting...")

    df = pd.read_csv(csv_file)
    ids = [i for i in df["id"]]
    fetch_download_links(ids)

if __name__ == "__main__":
    main()
