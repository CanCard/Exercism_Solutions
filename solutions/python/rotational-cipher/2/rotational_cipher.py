def rotate(text, key):
    """Encrypts the text using a Caesar cipher with the given key."""
    result = []
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            print(base)
            # Shift the character and wrap around the alphabet
            print( "ord(char)", ord(char))
            shifted = (ord(char) - base + key) % 26 + base
            # for 'A', A is 65, key is 23, shifted = (65 - 65 + 23) % 26 + 65 = (0 + 23) % 26 + 65 = 23 + 65 = 88
            print("shifted", shifted)
            print("chr(shifted)", chr(shifted))
            result.append(chr(shifted))
        else:
            # Non-alphabetic characters are not changed
            result.append(char)

    return ''.join(result)