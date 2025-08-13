def square_of_sum(number):
    sayi = number * (number + 1) / 2
    return sayi ** 2

def sum_of_squares(number):
    karesi = number * (number + 1) * (2*number + 1) / 6
    return karesi

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)