def generate_report(sequence, counts, percentages, weight):

    report = f"""
    =========================
    BioForge Protein Report
    =========================

    Sequence Length:
    {len(sequence)} amino acids

    Molecular Weight:
    {weight:.2f} Da

    Amino Acid Composition:
    """

    for amino_acid in counts:
        report += (
            f"\n{amino_acid}: "
            f"{percentages[amino_acid]:.2f}%"
        )

    return report