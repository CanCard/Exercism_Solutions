def score(x, y):
    if (abs(x) <= 1 and abs(y) <= 1) and abs(x) + abs(y) <= 1.5:
        return 10
    elif (abs(x) <= 5 and abs(y) <= 5) and abs(x) + abs(y) <= 7:
        return 5
    elif (abs(x) <=10 and abs(y) <= 10) and abs(x) + abs(y) <= 14:
        return 1
    else:
        return 0