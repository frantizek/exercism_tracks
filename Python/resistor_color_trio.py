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

def label(colors: list[str]) -> str:
    if len(colors) <=2:
        return "0 ohms"
    else:
        resistor_value_in_ohms = int(f"{str(int(RESISTOR_COLOR_VALUES[colors[0].lower()]))}{str(int(RESISTOR_COLOR_VALUES[colors[1].lower()]))}{"0"*(int(RESISTOR_COLOR_VALUES[colors[2].lower()]))}")
        if resistor_value_in_ohms < 1000:
            return f"{str(resistor_value_in_ohms)} ohms"
        elif 1000 < resistor_value_in_ohms >= 1000000:
            return f"{str(resistor_value_in_ohms)[0:-3]} kiloohms"
        elif 1000000 < resistor_value_in_ohms >= 1000000000:
            return f"{str(resistor_value_in_ohms)[0:-6]} megaohms"
        elif 1000000000 < resistor_value_in_ohms >= 1000000000000:
            return f"{str(resistor_value_in_ohms)[0:-9]} teraohms"
        return "0 ohms"
