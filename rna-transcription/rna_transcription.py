DNA_TO_RNA_MAP = str.maketrans('GCTA', 'CGAU')


def to_rna(dna: str) -> str:
    return dna.translate(DNA_TO_RNA_MAP)
