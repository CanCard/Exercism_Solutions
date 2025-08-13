def is_isogram(string):
    string = string.lower()
    string = string.replace("-","")
    string = string.replace(" ","")
    set_string = set(string)
    len_string = len(string)
    if len(set_string) == len_string:
        return True
    else:
        return False