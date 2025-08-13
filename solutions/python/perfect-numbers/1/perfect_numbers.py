def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    list = []
    #if type(number) == int:
    if number >= 1:
        for i in range(1, number):
            if (number % i == 0):
                list.append(i)
    
        if sum(list) == number:
            return "perfect"
        elif sum(list) > number:
            return "abundant"
        elif sum(list) < number:
            return "deficient"
    else:
        raise ValueError("Classification is only possible for positive integers.")
