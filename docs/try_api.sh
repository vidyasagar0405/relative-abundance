wget -O try_api.json "https://www.ebi.ac.uk/metagenomics/api/latest/biomes/root:Environmental:Aquatic:Marine/samples?experiment_type=metagenomic&metadata_key=temperature&metadata_value_lte=10&ordering=accession"

wget -O try_api_fecal.json "https://www.ebi.ac.uk/metagenomics/api/latest/biomes/root:Host-associated:Human:Digestive%20system:Large%20intestine:Fecal/samples?experiment_type=metagenomic&ordering=accession"

wget -O try_api_fecal_studies.json "https://www.ebi.ac.uk/metagenomics/api/latest/biomes/root:Host-associated:Human:Digestive%20system:Large%20intestine:Fecal/studies?experiment_type=metagenomic&ordering=accession"
