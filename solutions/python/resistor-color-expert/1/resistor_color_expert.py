def resistor_label(colors):
    color_digit = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }

    multipliers = {
        "black": 1,
        "brown": 10,
        "red": 100,
        "orange": 1_000,
        "yellow": 10_000,
        "green": 100_000,
        "blue": 1_000_000,
        "violet": 10_000_000,
        "grey": 100_000_000,
        "white": 1_000_000_000,
        "gold": 0.1,
        "silver": 0.01
    }

    tolerances = {
        "brown": "±1%",
        "red": "±2%",
        "green": "±0.5%",
        "blue": "±0.25%",
        "violet": "±0.1%",
        "grey": "±0.05%",
        "gold": "±5%",
        "silver": "±10%",
    }

    if len(colors) == 1:
        # Tek renk: sadece sayısal değer döner, tolerans yok
        return f"{color_digit[colors[0]]} ohms"

    elif len(colors) == 4:
        digits = color_digit[colors[0]] * 10 + color_digit[colors[1]]
        multiplier = multipliers[colors[2]]
        tolerance = tolerances[colors[3]]

    elif len(colors) == 5:
        digits = (color_digit[colors[0]] * 100 +
                  color_digit[colors[1]] * 10 +
                  color_digit[colors[2]])
        multiplier = multipliers[colors[3]]
        tolerance = tolerances[colors[4]]

    else:
        raise ValueError("Color band must be 1, 4 or 5")

    value = digits * multiplier

    # Birimi uygun şekilde bulalım
    if value >= 1_000_000_000:
        unit_value = value / 1_000_000_000
        unit = "gigaohms"
    elif value >= 1_000_000:
        unit_value = value / 1_000_000
        unit = "megaohms"
    elif value >= 1_000:
        unit_value = value / 1_000
        unit = "kiloohms"
    else:
        unit_value = value
        unit = "ohms"

    formatted = f"{unit_value:.2f}".rstrip("0").rstrip(".")

    return f"{formatted} {unit} {tolerance}"
