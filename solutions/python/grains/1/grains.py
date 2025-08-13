# 1) verilen karede kaç tahıl olacak (verilen satır üzeri 2) + raise ile hata döndürücen
# 2) tahtadaki toplam tahıl sayısını döndürücen

def square(a):
    if a > 0 and a < 65:
        return 2 ** (a - 1)
    else:
        raise ValueError("square must be between 1 and 64")

def total():
    a = 0
    t = 0
    for i in range(1,65):
        a = 2 ** (i - 1)
        t = a + t
    return t