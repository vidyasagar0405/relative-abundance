get_pubmed_id() {
    # Assign the provided argument to BIO_PROJ
    BIO_PROJ="$1"

    # Set the output file name based on the BioProject ID
    OUT="$BIO_PROJ.xml"

    # Fetch the BioProject XML from NCBI and write it to the output file
    efetch -db bioproject -id "$BIO_PROJ" -format xml > "$OUT"

    # Extract and print the Publication ID using xtract
    cat "$OUT" | xtract -pattern ProjectDescr -element Publication@id
}
