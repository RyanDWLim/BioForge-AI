from Bio import SeqIO

def read_fasta(file_path):

    record = SeqIO.read(
        file_path,
        "fasta"
    )

    return {
        "name": record.description,
        "sequence": str(record.seq)
    }