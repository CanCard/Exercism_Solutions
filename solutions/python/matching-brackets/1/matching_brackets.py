def is_paired(input_string: str) -> bool:
    # Kapanış parantezi -> uyumlu açılış parantezini eşle
    bracket_map = {")": "(", "]": "[", "}": "{"}
    openers = set(bracket_map.values())

    stack = []
    for ch in input_string:
        if ch in openers:
            stack.append(ch)
        elif ch in bracket_map:
            if not stack or stack.pop() != bracket_map[ch]:
                return False

    return not stack  # Yığın boşsa True, doluysa False
