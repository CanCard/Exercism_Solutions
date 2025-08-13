codon_table = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine", "UUG": "Leucine",
    "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
    "UAU": "Tyrosine", "UAC": "Tyrosine",
    "UGU": "Cysteine", "UGC": "Cysteine",
    "UGG": "Tryptophan"
}

def proteins(strand):
    empty = []
    last = []
    for char in range(0, len(strand),3):
        empty.append(strand[char:char+3])
    for codons in empty:
        if codons not in ("UAA", "UAG", "UGA"):
            last.append(codon_table.get(codons))
        else:
            break
    return last