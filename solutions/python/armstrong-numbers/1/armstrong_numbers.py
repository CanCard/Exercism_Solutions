def is_armstrong_number(number):
    list = [int(i) for i in str(number)]
    b = 0
    for i in list:
        a = i ** len(list)
        b = a + b
    if b == number:
        return True
    else:
        return False
    