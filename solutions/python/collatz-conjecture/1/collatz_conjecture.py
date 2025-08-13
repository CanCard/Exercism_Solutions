def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    else:
        sayac = 0
        while number != 1:
            if number % 2 == 0:
                number = number // 2
            elif number % 2 == 1:
                number = (number * 3) + 1
            sayac = sayac+1
        return sayac