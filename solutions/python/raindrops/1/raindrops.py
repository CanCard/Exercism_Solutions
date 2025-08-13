def convert(number):
    if (number % 3 == 0) and (number % 5 != 0 and number % 7 != 0):
        return "Pling"
    elif (number % 5 == 0) and (number % 3 != 0 and number % 7 != 0):
        return "Plang"
    elif (number % 7 == 0) and (number % 3 != 0 and number % 5 != 0):
        return "Plong"
    elif (number % 3 == 0) and (number % 5 == 0 and number % 7 != 0):
        return "PlingPlang"
    elif (number % 3 == 0) and (number % 7 == 0 and number % 5 != 0):
        return "PlingPlong"
    elif (number % 5 == 0) and (number % 7 == 0 and number % 3 != 0):
        return "PlangPlong"
    elif (number % 3 == 0) and (number % 5 == 0 and number % 7 == 0):
        return "PlingPlangPlong"
    else:
        return str(number)

# Her ihtimali yazmak yerine, en iyileri almak lazım.