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
    third = 10 ** int(str(color_list.index(colors[2])))

    deger = (one * 10 + two) * third

    if deger <= 1000000 and deger >= 1000:
        yazili_deger = f"{deger // 1000} kiloohms"
        return yazili_deger
    
    elif deger <= 1000000000 and deger >= 100000:
        yazili_deger = f"{deger // 1000000} megaohms"
        return yazili_deger
    
    elif deger >= 1000000000:
        yazili_deger = f"{deger // 1000000000} gigaohms"
        return yazili_deger
    
    else:
        yazili_deger = f"{deger} ohms"

    return yazili_deger