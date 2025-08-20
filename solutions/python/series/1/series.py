def slices(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")
    elif length < 0:
        raise ValueError("slice length cannot be negative")
    elif series == "":
        raise ValueError("series cannot be empty")
    elif len(series) < length:
        raise ValueError("slice length cannot be greater than series length")
    else:
        listem = []
        for i in range(0,len(series)+1):
            #print(series[i:length])
            listem.append(series[i:length])
            i += 1
            length += 1
            if length == len(series)+1:
                break
            else:
                continue
        return listem