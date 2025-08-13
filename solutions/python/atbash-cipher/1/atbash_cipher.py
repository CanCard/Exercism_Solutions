alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher = "zyxwvutsrqponmlkjihgfedcba"
punc = [".", "!", "?", "-", ",", "'"]

def encode(plain_text):
    sonuc = []
    for i in plain_text:
        if i.isdigit():
            sonuc.append(i)
            continue
        if i == " " or i in punc:
            continue
        else:
            c = alphabet.index(i.lower())
            e = alphabet[(len(alphabet) - 1) - c]
            sonuc.append(e)

    example = "".join(sonuc)
    example_1 = ' '.join([example[i:i+5] for i in range(0, len(example), 5)])
    return example_1

def decode(ciphered_text):
    sonuc = []
    for i in ciphered_text:
        if i.isdigit():
            sonuc.append(i)
            continue
        if i == " " or i in punc:
            continue
        else:
            c = alphabet.index(i.lower())
            e = alphabet[(len(cipher) - 1) - c]
            sonuc.append(e)

    return "".join(sonuc)
