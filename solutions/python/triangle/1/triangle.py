def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if ((a + b >= c) and (b + c >= a) and (a + c >= b)) and (a > 0 and b > 0 and c > 0) and (a == b == c):
        return True
    else:
        return False


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if ((a + b >= c) and (b + c >= a) and (a + c >= b)) and (a > 0 and b > 0 and c > 0) and ((a == b) or (b == c) or (c == a)):
        return True
    else:
        return False


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if ((a + b >= c) and (b + c >= a) and (a + c >= b)) and (a > 0 and b > 0 and c > 0) and ((a != b) and (b != c) and (c != a) and (a != b != c)):
        return True
    else:
        return False
