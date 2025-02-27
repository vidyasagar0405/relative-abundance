from Bio import Entrez
import xml.etree.ElementTree as ET

# Set your email (required by NCBI)
Entrez.email = "your_email@example.com"

def get_bioproject_numeric_id(accession):
    """
    Given a BioProject accession, use esearch to obtain the numeric ID.
    """
    handle = Entrez.esearch(db="bioproject", term=accession)
    record = Entrez.read(handle)
    handle.close()
    if record["IdList"]:
        return record["IdList"][0]
    else:
        return None

def get_pubmed_id(accession):
    """
    Given a BioProject accession, first get its numeric ID, then fetch the XML and
    extract the PubMed ID from the <Publication> element within <ProjectDescr>.
    """
    bioproject_id = get_bioproject_numeric_id(accession)
    if not bioproject_id:
        return f"BioProject numeric ID for accession {accession} not found."

    # Fetch the BioProject XML using the numeric ID
    handle = Entrez.efetch(db="bioproject", id=bioproject_id, rettype="xml")
    xml_data = handle.read()
    handle.close()

    # Parse the XML
    root = ET.fromstring(xml_data)

    # Look for the <Publication> element inside <ProjectDescr>
    pub_elem = root.find(".//ProjectDescr/Publication")
    if pub_elem is not None and 'id' in pub_elem.attrib:
        print("PubMed ID:", pub_elem.attrib['id'])
        return pub_elem.attrib['id']
    else:
        return "No PubMed ID found"

# Example usage:
if __name__ == "__main__":
    accession = "PRJEB26832"  # Replace with your actual BioProject accession
    pubmed_id = get_pubmed_id(accession)
    print("PubMed ID:", pubmed_id)
