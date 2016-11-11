DNA_TO_RNA_MAP = str.maketrans('GCTA', 'CGAU')


def to_rna(dna):
    return dna.translate(DNA_TO_RNA_MAP)
