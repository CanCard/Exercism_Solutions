points = dict.fromkeys(["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], 1)
points.update(dict.fromkeys(["D", "G"], 2))
points.update(dict.fromkeys(["B", "C", "M", "P"], 3))
points.update(dict.fromkeys(["F", "H", "V", "W", "Y"], 4))
points.update(dict.fromkeys(["K"], 5))
points.update(dict.fromkeys(["J", "X"], 8))
points.update(dict.fromkeys(["Q", "Z"], 10))

def score(word):
    a = 0
    word = word.upper()
    for i in word:
        print(i)
        a += points.get(i)
    return a