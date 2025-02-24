from jsonapi_client import Session
import pandas as pd
import matplotlib.pyplot as plt

accession = "MGYS00002236"
accessions = ["MGYS00002236", "MGYS00006219"]
base_url = "https://www.ebi.ac.uk/metagenomics/api/v1"
downloads = f"/studies/{accession}/downloads"


def fetch_analyses(accession, base_url=base_url):
    with Session(base_url) as mgnify:
        analyses_list = []
        for response in mgnify.iterate(f'studies/{accession}/analyses'):
            try:
                # Attempt to get the JSON from the response
                data = response.json
                analyses_list.append(data)
            except Exception as e:
                print("Error decoding JSON for a response:")
                print(response.text)  # Log the raw response for debugging
                raise e
        # Normalize the collected JSON objects into a DataFrame
        analyses_df = pd.json_normalize(analyses_list)
    return analyses_df

def create_links(accession:list[str]) -> dict[str, str]:

    full_study_links: dict = {}
    for id in accession:
        full_study_links[id] = f"{base_url}studies/{id}/downloads"

    for id, link in full_study_links.items():
        print(f"IDs found {id}: {link}")

    return full_study_links

def main():
    create_links(accessions)

    for accession in accessions:
        try:
            df = fetch_analyses(accession)
            print(df.head())
        except Exception as error:
            print(f"Failed to fetch analyses: {error}")

        df.to_csv(f"{accession}.csv")
        df.groupby('attributes.samples-count').size().plot(kind='pie')
        plt.title('Number of Analysed Samples by instrument type')
        plt.savefig(f"Number_of_Analysed_Samples_by_instrument_type_in_{accession}.svg")


if __name__ == "__main__":
    main()
