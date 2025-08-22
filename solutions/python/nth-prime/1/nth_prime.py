def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")
    count = 0
    num = 2  # asal sayılar 2'den başlar
    while True:
        is_prime = True
        for i in range(2, int(num**0.5) + 1): # Bir sayının bölenlerini sadece kareköküne kadar kontrol etmek yeterlidir. 
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
            if count == number:
                return num
        num += 1
