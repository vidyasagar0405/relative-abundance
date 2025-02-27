#!/bin/bash

get_pubmed_id() {
    # Assign the provided argument to BIO_PROJ
    BIO_PROJ="$1"

    # Set the output file name based on the BioProject ID
    OUT="${BIO_PROJ}.xml"

    # Fetch the BioProject XML from NCBI and write it to the output file
    efetch -db bioproject -id "$BIO_PROJ" -format xml > "$OUT"

    # Extract the Publication ID using xtract
    pubmed_id=$(cat "$OUT" | xtract -pattern ProjectDescr -element Publication@id)

    # If no PubMed ID is found, echo NaN
    if [ -z "$pubmed_id" ]; then
        echo "NaN"
    else
        echo "$pubmed_id"
    fi
}

main() {
    file="$1"

    # Extract the third field (comma-separated) containing the BioProject accession IDs
    ids=$(cut -f3 -d, "$file")

    for id in $ids; do
        pubmed_id=$(get_pubmed_id "$id")
        echo "$id,$pubmed_id"
    done
}

main "$@"
