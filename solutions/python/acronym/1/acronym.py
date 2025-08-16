def abbreviate(words):
    
    table = str.maketrans("", "", ".,!?'/_")
    words = words.translate(table)
    
    acronym = ""
    res = words.split("-")
    
    jes = " ".join(res)
    mes = jes.split()
    print(mes)
    for i in mes:
        m = i[0]
        acronym = acronym + m
    return acronym.upper()