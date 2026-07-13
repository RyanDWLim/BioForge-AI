def read_fasta(file_path):

    sequence = ""

    with open(file_path, "r") as file:

        for line in file:

            line = line.strip()

            # Ignore the description line
            if line.startswith(">"):
                continue

            # Add sequence lines
            sequence += line

    return sequence