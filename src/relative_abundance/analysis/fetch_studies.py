from jsonapi_client import Session
import pandas as pd
import matplotlib.pyplot as plt

accession = "MGYS00002236"
accessions = ["MGYS00002236", "MGYS00006219"]
base_url = "https://www.ebi.ac.uk/metagenomics/api/latest"
downloads = f"/studies/{accession}/downloads"
biome = "root:Host-associated:Human:Digestive%20system:Large%20intestine:Fecal"


link = f"https://www.ebi.ac.uk/metagenomics/api/latest/biomes/{biome}/studies?experiment_type=metagenomic&ordering=accession"

def fetch_analyses(biome, base_url=base_url):
    with Session(base_url) as mgnify:
        analyses_list = []
        for response in mgnify.iterate(f'biomes/{biome}/studies?experiment_type=metagenomic&ordering=accession"'):
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

def main():

    try:
        df = fetch_analyses(biome)
        print(df.head())
    except Exception as error:
        print(f"Failed to fetch analyses: {error}")

    df.to_csv(f"{biome}.csv")
    df.groupby('attributes.samples-count').plot(kind='bar')
    plt.title('Number of Analysed Samples by instrument type')
    plt.savefig(f"Number_of_Analysed_Samples_in_{biome}_bar.svg")


if __name__ == "__main__":
    main()
