def to_rna(dna_strand):
    liste = list(dna_strand)
    sonuc = []

    for i in liste:
        if i == "G":
            sonuc.append("C")
        elif i == "C":
            sonuc.append("G")
        elif i == "T":
            sonuc.append("A")
        elif i == "A":
            sonuc.append("U")
        else:
            return ""
    return "".join(sonuc)