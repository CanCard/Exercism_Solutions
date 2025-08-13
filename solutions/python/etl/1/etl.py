def transform(legacy_data):
    res = {}
    for value in legacy_data.keys():
        for a in legacy_data[value]:
            res[a.lower()] = value
    return res
