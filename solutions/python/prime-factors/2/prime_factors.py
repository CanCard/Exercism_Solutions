def factors(value):
    factors_list = []
    kalan = value

    i = 2
    while kalan != 1:
        if kalan % i == 0:
            factors_list.append(i)
            kalan = kalan // i
        if kalan % i != 0:
            i = i + 1
    return factors_list