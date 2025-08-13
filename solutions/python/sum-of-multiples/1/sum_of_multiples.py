def sum_of_multiples(limit, multiples):
    limit = limit - 1
    kume = set()
    for i in multiples:
        if i == 0:
            continue
        else:
            y = limit // i
            for m in range(1, y + 1):
                sonuc = i * m
                kume.add(sonuc)
    return(sum(kume))