def is_valid(isbn):
    isbn = isbn.replace("-", "")  # tireleri kaldır
    if len(isbn) != 10:
        return False
    toplam = 0
    for i in range(10):
        char = isbn[i]
        if i == 9 and char.upper() == 'X':
            deger = 10
        elif char.isdigit():
            deger = int(char)
        else:
            return False  # Geçersiz karakter varsa hemen False dön
        katsayi = 10 - i
        toplam += deger * katsayi

    return toplam % 11 == 0
