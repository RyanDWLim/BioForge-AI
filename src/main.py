from protein import (
    validate_sequence,
    sequence_length,
    count_amino_acids,
    amino_acid_percentage,
    molecular_weight
)

from fasta_reader import read_fasta

from report import generate_report

from uniprot import get_protein_from_uniprot

protein_id = input(
    "Enter UniProt ID: "
)

protein = get_protein_from_uniprot(
    protein_id
)

sequence = protein["sequence"]

protein_name = protein["name"]

#---------------------------------------------------
print("BioForge Protein Analyzer")
print("------------------------")

if validate_sequence(sequence):

    print("Valid protein sequence")

    print(
        "Length:",
        sequence_length(sequence)
    )

    print(
        "Amino Acid Count:",
        count_amino_acids(sequence)
    )

    print(
        "Percentages:",
        amino_acid_percentage(sequence)
    )

    counts = count_amino_acids(sequence)

    percentages = amino_acid_percentage(sequence)

    weight = molecular_weight(sequence)


    print(
        generate_report(
            protein_name,
            sequence,
            counts,
            percentages,
            weight
        )
    )

else:

    print("Invalid sequence")

