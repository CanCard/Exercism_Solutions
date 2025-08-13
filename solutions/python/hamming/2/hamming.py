def distance(strand_a, strand_b):
    sayi = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    else:
        for i,y in zip(strand_a, strand_b):
            if i!=y:
                sayi = sayi + 1
        return sayi