def factors(value):
    factors_list = []
    kalan = value

    # 2'leri çıkar
    while kalan % 2 == 0:
        factors_list.append(2)
        kalan //= 2

    # Tek sayıları kontrol et, sadece √kalan'a kadar
    i = 3
    while i * i <= kalan:
        while kalan % i == 0:
            factors_list.append(i)
            kalan //= i
        i += 2  # sadece tek sayılar

    # Kalan > 1 ise asal çarpandır
    if kalan > 1:
        factors_list.append(kalan)

    return factors_list
