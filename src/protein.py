AMINO_ACIDS = {
    "A": "Alanine",
    "R": "Arginine",
    "N": "Asparagine",
    "D": "Aspartic Acid",
    "C": "Cysteine",
    "E": "Glutamic Acid",
    "Q": "Glutamine",
    "G": "Glycine",
    "H": "Histidine",
    "I": "Isoleucine",
    "L": "Leucine",
    "K": "Lysine",
    "M": "Methionine",
    "F": "Phenylalanine",
    "P": "Proline",
    "S": "Serine",
    "T": "Threonine",
    "W": "Tryptophan",
    "Y": "Tyrosine",
    "V": "Valine"
}

AMINO_ACID_WEIGHTS = {
    "A":89.09,
    "R":174.20,
    "N":132.12,
    "D":133.10,
    "C":121.15,
    "E":147.13,
    "Q":146.15,
    "G":75.07,
    "H":155.16,
    "I":131.17,
    "L":131.17,
    "K":146.19,
    "M":149.21,
    "F":165.19,
    "P":115.13,
    "S":105.09,
    "T":119.12,
    "W":204.23,
    "Y":181.19,
    "V":117.15
}

# Function to check if a protein sequence contains valid amino acids
# Boolean function
def validate_sequence(sequence):

    sequence = sequence.upper()

    for amino_acid in sequence:
        if amino_acid not in AMINO_ACIDS:
            return False

    return True

# Function to return length of protein sequence
# Returns as int var
def sequence_length(sequence):
    return len(sequence)

# Function that returns count of each amino acid in protein sequence
# Returns as dict var
def count_amino_acids(sequence):

    counts = {}

    for amino_acid in sequence:

        if amino_acid in counts:
            counts[amino_acid] += 1

        else:
            counts[amino_acid] = 1

    return counts

# Function to calc percentages of each amino acid
# Returns as dict var
def amino_acid_percentage(sequence):

    counts = count_amino_acids(sequence)

    percentages = {}

    total = len(sequence)

    for amino_acid in counts:
        percentages[amino_acid] = (
            counts[amino_acid] / total
        ) * 100

    return percentages


# Function to calculate molecular weight of protein sequence
# Returns as float var
def molecular_weight(sequence):

    weight = 0

    for amino_acid in sequence:
        weight += AMINO_ACID_WEIGHTS[amino_acid]

    return weight