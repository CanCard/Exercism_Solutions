import re

def count_words(sentence):
    
    sentence = sentence.lower()
    sentence = re.sub(r',', ' ', sentence)
    sentence = re.sub(r'_', ' ', sentence)
    sentence = re.sub(r"[^\w\s']", '', sentence)
    sentence = re.sub(r'\s+', ' ', sentence)
    sentence = sentence.strip().split(" ")
    sentence[0] = sentence[0].strip("'")
    sentence[-1] = sentence[-1].strip("'")
    
    sonuc = {}

    for i in sentence:
        if i == "":
            continue
        if i[0] == "'" and i[-1] == "'":
            i = i[1:-1]
        if i:
            sonuc[i] = sonuc.get(i,0) + 1
        
    return sonuc