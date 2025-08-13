import string

ALPHABET = list(string.ascii_uppercase)  # A-Z, J dahil

def rows(letter):
    if letter not in ALPHABET:
        return []
    
    max_index = ALPHABET.index(letter)
    width = max_index * 2 + 1
    lines = []

    # ÜST YARI
    for i in range(max_index + 1):
        line = [" "] * width
        line[max_index - i] = ALPHABET[i]
        line[max_index + i] = ALPHABET[i]
        lines.append("".join(line))

    # ALT YARI
    for i in range(max_index - 1, -1, -1):
        lines.append(lines[i])

    return lines
