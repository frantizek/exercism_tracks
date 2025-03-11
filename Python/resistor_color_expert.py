TOLERANCE_VALUES = {
"grey" : "0.05%",
"violet" : "0.1%",
"blue" : "0.25%",
"green" : "0.5%",
"brown" : "1%",
"red" : "2%",
"gold" : "5%",
"silver" : "10%"
}


RESISTOR_COLOR_VALUES = {
"black": 0,
"brown": 1,
"red": 2,
"orange": 3,
"yellow": 4,
"green": 5,
"blue": 6,
"violet": 7,
"grey": 8,
"white": 9
}

def resistor_label(colors: list[str]) -> str:
    resistor_bands = len(colors)
    match resistor_bands:
        case 1:
            return "0 ohms"
        case 4:
            resistor_value_in_ohms = int(
                f"{str(int(RESISTOR_COLOR_VALUES[colors[0].lower()]))}{str(int(RESISTOR_COLOR_VALUES[colors[1].lower()]))}{'0' * (int(RESISTOR_COLOR_VALUES[colors[2].lower()]))}")
            if resistor_value_in_ohms < 1000:
                return f"{resistor_value_in_ohms} ohms ±{TOLERANCE_VALUES[colors[3].lower()]}"
            elif 1000 <= resistor_value_in_ohms < 1000000:
                if (resistor_value_in_ohms / 1000).is_integer():
                    return f"{int(resistor_value_in_ohms / 1000)} kiloohms ±{TOLERANCE_VALUES[colors[3].lower()]}"
                return f"{resistor_value_in_ohms / 1000} kiloohms ±{TOLERANCE_VALUES[colors[3].lower()]}"
            elif 1000000 <= resistor_value_in_ohms < 1000000000:
                return f"{resistor_value_in_ohms / 1000000} megaohms ±{TOLERANCE_VALUES[colors[3].lower()]}"
            elif 1000000000 <= resistor_value_in_ohms < 1000000000000:
                return f"{resistor_value_in_ohms / 1000000000} gigaohms ±{TOLERANCE_VALUES[colors[3].lower()]}"
            else:
                return f"{resistor_value_in_ohms / 1000000000000} teraohms ±{TOLERANCE_VALUES[colors[3].lower()]}"
        case 5:
            resistor_value_in_ohms = int(
                f"{str(int(RESISTOR_COLOR_VALUES[colors[0].lower()]))}{str(int(RESISTOR_COLOR_VALUES[colors[1].lower()]))}{str(int(RESISTOR_COLOR_VALUES[colors[2].lower()]))}{'0' * (int(RESISTOR_COLOR_VALUES[colors[3].lower()]))}")
            if resistor_value_in_ohms < 1000:
                return f"{resistor_value_in_ohms} ohms ±{TOLERANCE_VALUES[colors[4].lower()]}"
            elif 1000 <= resistor_value_in_ohms < 1000000:
                if (resistor_value_in_ohms / 1000).is_integer():
                    return f"{int(resistor_value_in_ohms / 1000)} kiloohms ±{TOLERANCE_VALUES[colors[4].lower()]}"
                return f"{resistor_value_in_ohms / 1000} kiloohms ±{TOLERANCE_VALUES[colors[4].lower()]}"
            elif 1000000 <= resistor_value_in_ohms < 1000000000:
                return f"{resistor_value_in_ohms / 1000000} megaohms ±{TOLERANCE_VALUES[colors[4].lower()]}"
            elif 1000000000 <= resistor_value_in_ohms < 1000000000000:
                return f"{resistor_value_in_ohms / 1000000000} gigaohms ±{TOLERANCE_VALUES[colors[4].lower()]}"
            else:
                return f"{resistor_value_in_ohms / 1000000000000} teraohms ±{TOLERANCE_VALUES[colors[4].lower()]}"
        case _:
            return ""
