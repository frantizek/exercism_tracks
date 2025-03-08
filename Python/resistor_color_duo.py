# The first 2 bands of a resistor have a simple encoding scheme:
# each color maps to a single number.
# For example, if they printed a brown band (value 1)
# followed by a green band (value 5),
# it would translate to the number 15.
#
# In this exercise you are going to create a helpful program
# so that you don't have to remember the values of the bands.
# The program will take color names as input and output a
# two digit number, even if the input is more than two colors!
#
# The band colors are encoded as follows:
#
# black: 0
# brown: 1
# red: 2
# orange: 3
# yellow: 4
# green: 5
# blue: 6
# violet: 7
# grey: 8
# white: 9

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

def value(colors: list[str]) -> int:
    if len(colors) <=1:
        return 0
    else:
        return int(f"{str(int(RESISTOR_COLOR_VALUES[colors[0].lower()]))}{str(int(RESISTOR_COLOR_VALUES[colors[1].lower()]))}")
