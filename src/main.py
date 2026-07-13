from protein import (
    validate_sequence,
    sequence_length,
    count_amino_acids,
    amino_acid_percentage,
    molecular_weight
)

from fasta_reader import read_fasta

sequence = read_fasta(
    "data/raw/hemoglobin.fasta"
)

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

    print(
        "Molecular Weight:",
        molecular_weight(sequence),
        "Da"
    )

else:

    print("Invalid sequence")

