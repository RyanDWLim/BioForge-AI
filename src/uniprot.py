import requests


def get_protein_from_uniprot(protein_id):

    # Create UniPROT URL
    url = (
        f"https://rest.uniprot.org/"
        f"uniprotkb/{protein_id}.fasta"
    )

    response = requests.get(url)


    if response.status_code != 200:
        raise Exception(
            "Protein not found"
        )


    lines = response.text.splitlines()


    name = lines[0][1:]

    sequence = "".join(
        lines[1:]
    )

    # Reading FASTA response and returning as dict
    return {
        "name": name,
        "sequence": sequence
    }