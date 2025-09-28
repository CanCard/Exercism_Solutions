def transpose(text):
    new_text = ""
    if "\n" not in text:
        for i in text:
            if i == text[-1]:
                new_text = new_text + i
            else:
                new_text = new_text + i + "\n"
        return new_text
        
    second_text = ""
    parts = text.split("\n")
    max_len = max(len(p) for p in parts)

    for i in range(max_len):
        for part in parts:
            if i < len(part):
                second_text += part[i]
            else:
                second_text += "#"
        # son sütunda yeni satır ekleme
        second_text = second_text.rstrip("#")
        if i != max_len - 1:
            second_text += "\n"

    return second_text.replace("#"," ")