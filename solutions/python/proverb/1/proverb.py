def proverb(*input_data, qualifier=None):
    if not input_data:
        return []
    a, *last = input_data
    listem = []

    
    if len(input_data) == 1:
        if qualifier:
            listem.append(f"And all for the want of a {qualifier} {a}.")
        else:
            listem.append(f"And all for the want of a {a}.")
    
    for previous, current in zip(input_data, input_data[1:]):
        listem.append(f"For want of a {previous} the {current} was lost.")
        if current == input_data[-1]:
            if qualifier:
                listem.append(f"And all for the want of a {qualifier} {a}.")
            else:
                listem.append(f"And all for the want of a {a}.")
    return listem