#!/usr/bin/env bash

conda create -n mgnify-api python=3.8
conda activate mgnify-api
pip install pandas numpy scipy plotnine jsonapi-client mg-toolkit requests
curl http://ftp.ebi.ac.uk/pub/databases/metagenomics/mgnify_courses/ebi_2020/api.tar.gz | tar xz --strip 1
