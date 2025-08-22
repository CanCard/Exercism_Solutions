def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")
    n = 0
    sayi = 1
    number_checker = 0
    while number_checker != number:
        sayi += 1
        for k in range(2,int(sayi**0.5)+1):
            if sayi % k == 0:                
                break
        else:
            n = sayi
            number_checker += 1
    return n