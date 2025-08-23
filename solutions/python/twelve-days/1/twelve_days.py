expected = {
            12: "twelve Drummers Drumming, ",
            11: "eleven Pipers Piping, ",
            10: "ten Lords-a-Leaping, ",
            9: "nine Ladies Dancing, ",
            8: "eight Maids-a-Milking, ",
            7: "seven Swans-a-Swimming, ",
            6: "six Geese-a-Laying, ",
            5: "five Gold Rings, ",
            4: "four Calling Birds, ",
            3: "three French Hens, ",
            2: "two Turtle Doves, ",
            1: "a Partridge in a Pear Tree."
}

words = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth", 7: "seventh", 8: "eighth", 9: "ninth", 10: "tenth", 11: "eleventh", 12: "twelfth"}

def recite(start_verse, end_verse):
    result = []
    for day in range(start_verse, end_verse + 1):
        my_string = ""
        for i in range(day, 0, -1):
            if i == 1 and day != 1:  # 1. gün hariç, 1 numaralı hediyeye "and " ekle
                my_string += "and " + expected[i]
            else:
                my_string += expected[i]
        result.append(f"On the {words[day]} day of Christmas my true love gave to me: {my_string}")
    return result