def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    list_a = []
    list_b = []
    
    for c in strand_a:
        list_a.append(c)
    for c in strand_b:
        list_b.append(c)
    if list_a == list_b:
        return 0

    sayi = 0

    for i in range(len(list_a)):
        if list_a[i] != list_b[i]:
            sayi = sayi + 1
    return sayi