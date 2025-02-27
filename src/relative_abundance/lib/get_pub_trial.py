import pandas as pd
from relative_abundance.lib.get_publication import get_pubmed_id

def main():

    df = pd.read_csv("../analysis/fetch_studies/amplicon/fetch_studies_amplicon.csv")

    df["pubmed-id"] = df["bioproject"].apply(get_pubmed_id)

    df.to_csv("../analysis/fetch_studies/amplicon/fetch_studies_amplicon_pmid.csv")

if __name__ == "__main__":
    main()
