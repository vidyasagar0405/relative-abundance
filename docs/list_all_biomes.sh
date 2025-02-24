#!/usr/bin/env bash

 > available_biomes.csv

for page in {1..20}; do
    curl -X GET https://www.ebi.ac.uk/metagenomics/api/v1/biomes?page="$page" | jq '.data[].id' | sed 's/"//g' >> available_biomes.csv
done
