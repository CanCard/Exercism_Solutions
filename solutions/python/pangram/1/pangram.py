def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = []
    alphabet = "".join(chr(i) for i in range(ord('a'), ord("z")+1))
    result = set(alphabet).issubset(set(sentence))
    if result == True:
        return True
    else:
        return False