say_dict = {
    0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve",
    13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty",
    50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"
}

def say(number):
    length = len(str(number)) # to see the length of the number
    str_number = str(number)
    
    
    if number < 0 or number > 999999999999: # 12 digits
        raise ValueError("input out of range")

    if length == 1:
        return say_dict.get(number)
    
    if length == 2:
        if 10<= number <= 19:
            return say_dict.get(number)
        if str_number[1] != "0":
            word = str_number[0] + "0" + str_number[1]
            first = int(word[0:2])
            last = int(word[-1])
            return say_dict.get(first) + "-" + say_dict.get(last)
        else:
            return say_dict.get(number)
    
    if length == 3:
        hundreds = int(str_number[0])
        rest = int(str_number[1:])

        if rest == 0:
            return say_dict[hundreds] + " hundred"
        else:
            return say_dict[hundreds] + " hundred " + say(rest)
    
    if length == 4:
        thousands = int(str_number[0])
        rest = int(str_number[1:])
        if rest == 0:
            return say_dict[thousands] + " thousand"
        else:
            return say_dict[thousands] + " thousand " + say(rest)

    if length == 5:
        two_digit = int(str_number[0:2])
        rest = int(str_number[2:])
        if rest == 0:
            return say(two_digit) + " thousand"
        else:
            return say(two_digit) + " thousand " + say(rest)
        
    if length == 6:
        first = int(str_number[0:3])
        last = int(str_number[3:])

        if last == 0:
            return say(first) + " thousand"
        else:
            return say(first) + " thousand " + say(last)
    
    if length == 7:
        first = int(str_number[0])
        mid = int(str_number[1:4])
        last = int(str_number[4:])
        print(first, mid, last)

        if (mid == 0) and (last == 0):
            return say(first) + " million"
        elif last == 0:
            return say(first) + " million " + say(mid) + " thousand "
        else:
            return say(first) + " million " + say(mid) + " thousand " + say(last)
        
    if length == 8:
        first = int(str_number[0:2])
        mid = int(str_number[2:5])
        last = int(str_number[5:])

        if (mid == 0) and (last == 0):
            return say(first) + " million"
        elif last == 0:
            return say(first) + " million " + say(mid) + " thousand "
        else:
            return say(first) + " million " + say(mid) + " thousand " + say(last)
        
    if length == 9:
        first = int(str_number[0:3])
        mid = int(str_number[3:6])
        last = int(str_number[6:])

        if (mid == 0) and (last == 0):
            return say(first) + " million"
        elif last == 0:
            return say(first) + " million " + say(mid) + " thousand "
        else:
            return say(first) + " million " + say(mid) + " thousand " + say(last)
    
    if length == 10:
        first = int(str_number[0])
        mid = int(str_number[1:4])
        mid_2 = int(str_number[4:7])
        last = int(str_number[7:])
        print(first, mid, mid_2, last)

        if (mid == 0) and (last == 0) and (mid_2 == 0):
            return say(first) + " billion"
        elif mid_2 == 0 and last == 0:
            return say(first) + " billion " + say(mid) + " million " 
        elif last == 0:
            return say(first) + " billion " + say(mid) + " million " + say(mid_2) + " thousand "
        else:
            return say(first) + " billion " + say(mid) + " million " + say(mid_2) + " thousand " + say(last)
    
    if length == 11:
        first = int(str_number[0:2])
        mid = int(str_number[2:5])
        mid_2 = int(str_number[5:8])
        last = int(str_number[8:])
        print(first, mid, mid_2, last)

        if (mid == 0) and (last == 0) and (mid_2 == 0):
            return say(first) + " billion"
        elif mid_2 == 0 and last == 0:
            return say(first) + " billion " + say(mid) + " million " 
        elif last == 0:
            return say(first) + " billion " + say(mid) + " million " + say(mid_2) + " thousand "
        else:
            return say(first) + " billion " + say(mid) + " million " + say(mid_2) + " thousand " + say(last)
    
    if length == 12:
        first = int(str_number[0:3])
        mid = int(str_number[3:6])
        mid_2 = int(str_number[6:9])
        last = int(str_number[9:])
        print(first, mid, mid_2, last)

        if (mid == 0) and (last == 0) and (mid_2 == 0):
            return say(first) + " billion"
        elif mid_2 == 0 and last == 0:
            return say(first) + " billion " + say(mid) + " million " 
        elif last == 0:
            return say(first) + " billion " + say(mid) + " million " + say(mid_2) + " thousand "
        else:
            return say(first) + " billion " + say(mid) + " million " + say(mid_2) + " thousand " + say(last)
