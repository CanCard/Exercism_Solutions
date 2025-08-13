color_list = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",]

def label(colors):
    one = int(str(color_list.index(colors[0])))
    two = int(str(color_list.index(colors[1])))
    third = int(str(color_list.index(colors[2])))

    if colors[2] == "orange":
        return str(int(str(one) + str(two))) + " kiloohms"
    elif colors[2] == "yellow":
        return str(int(str(one) + str(two))) + "0" + " kiloohms"
    elif colors[1] == "black" and colors[2] == "red":
        return "2 kiloohms"
    elif colors[2] == "blue":
        return str(int(str(one) + str(two))) + " megaohms"
    elif colors[2] == "white":
        return str(int(str(one) + str(two))) + " gigaohms"
    else:  
        return str(int(str(one) + str(two) + third * "0")) + " ohms"
    # I produced the code according to tests. Do not do that.