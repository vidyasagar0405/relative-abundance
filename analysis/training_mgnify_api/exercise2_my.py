#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import csv
from jsonapi_client import Session, Filter

from plotnine import *
import pandas

API_BASE = "https://www.ebi.ac.uk/metagenomics/api/v1"

TAX_RANK = "phylum"


# MGYS00001211 (SRP076746) Human gut metagenome Metagenome
study_accession = "MGYS00001211"

# MGYS00000601 (ERP013908) Assessment of Bacterial DNA Extraction Procedures for Metagenomic Sequencing Evaluated
# on Different Environmental Matrices.
# study_accession = "MGYS00000601"

resource = "studies/" + study_accession + "/analyses"

rows = []

with Session(API_BASE) as session:
    # TODO: iterate?
    analyses = session.get(resource).resources

    analyses_accs = [a.accession for a in analyses]

    # Select individual analyses, e.g. OSD
    # analyses_accs = [""]

    for analysis_accession in analyses_accs:

        tax_annotations = session.get(
            "/".join(["analyses", analysis_accession, "taxonomy", "ssu"])
        ).resources

        for t in tax_annotations:
            rows.append(
                {
                    "analysis": analysis_accession,
                    "study": study_accession,
                    TAX_RANK: t.hierarchy.get(TAX_RANK),
                    "count": t.count,
                    "rel_abundance": 0,  # this will be filled afterwards
                },
            )
    data_frame = pandas.DataFrame(rows)

    # let's aggregate by Phyla
    data_frame = data_frame.groupby(["analysis", TAX_RANK])["count"].sum().reset_index()

    # let's get the relative abundance of each phyla
    for analysis, frame in data_frame.groupby("analysis"):
        data_frame.loc[data_frame["analysis"] == analysis, "rel_abundance"] = (
            frame["count"] / frame["count"].sum() * 100
        )

    # let's save a copy in csv
    data_frame.to_csv(study_accession + "_" + TAX_RANK + ".csv")
