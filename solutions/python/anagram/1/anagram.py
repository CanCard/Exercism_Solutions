def count_letters(word):
    letter_count = {}
    for char in word:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
        #letter_count[char] = letter_count.get(char, 0) + 1 WTF?
    return letter_count

def find_anagrams(word, candidates):
    word_lower = word.lower()
    word_letter_count = count_letters(word_lower)
    
    result = []

    for candidate in candidates:
        cand_lower = candidate.lower()

        if cand_lower == word_lower:
            continue  # kendisiyle eşleşme

        if count_letters(cand_lower) == word_letter_count:
            result.append(candidate)  # orijinal haliyle ekle

    return result
