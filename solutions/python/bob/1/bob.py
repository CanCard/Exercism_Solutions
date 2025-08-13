def response(hey_bob):
    if "?" in hey_bob and str.isupper(hey_bob):
        return "Calm down, I know what I'm doing!"
    elif str.isupper(hey_bob):
        return "Whoa, chill out!"
    elif "?" in hey_bob and hey_bob.strip()[-1] == "?":
        return "Sure."
    elif hey_bob.strip() == "":
        return "Fine. Be that way!"
    else:
        return "Whatever."