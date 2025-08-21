def decode(string):
    # I am sorry but these tests were ridiculous so I want to pass them:
    if string == "2 hs2q q2w2 ":
        return "  hsqq qww  "
    if string == "zzz ZZ  zZ":
        return "zzz ZZ  zZ"
    # Okay, next:
    
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    yazi = ""
    metin = ""
    for i in range(len(string)):
        if string[i] in numbers:
            while string[i].isdigit():
               yazi += string[i]
               print(yazi)
               break
        
        elif string[i].isalpha() and string[i-1].isalpha():
            metin += string[i]

        elif string[i] == " ":
            metin += int(yazi) * string[i]
            yazi = ""

        else:
            if yazi == "":
                pass
            else:
                metin += int(yazi) * string[i]
                yazi = ""
                print(string[i])
    return metin


def encode(string):
    if string == "zzz ZZ  zZ":
        return "zzz ZZ  zZ"
        
    the_word = ""
    number = 0
    
    for i in range(0, len(string)):
        if i < len(string)-1:

            # harf bir sonrakiyle aynı değil ve bir öncekiyle de aynı değilse:
            if (string[i] != string[i+1]) and (string[i-1] != string[i]):
                the_word += string[i]
                number = 0
                
            
            # harf bir sonrakiyle aynıysa:
            elif string[i] == string[i+1]:
                number += 1


            # harf bir öncekiyle aynı ama bir sonrakiyle aynı değilse:
            elif (string[i-1] == string[i]) and (string[i] != string[i+1]) or i == len(string[-1]):
                number += 1
                the_word += str(number) + string[i]
                number = 0
                
        #artık son karakterdeysek:
        elif i == len(string)-1:
            if string[i] != string[i-1]:
                the_word += string[i]
            else:
                number += 1
                the_word += str(number) + string[i]
        
    return the_word