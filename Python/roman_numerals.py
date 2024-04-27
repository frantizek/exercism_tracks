def roman(number: int) -> str:
    # First, validate if the number is within the valid range
    if number < 0 or number >= 4000:
        return "Error"
    else:
        if number >= 1000:
            return "M" + roman(number-1000)
        elif number >= 900:
            return "CM" + roman(number-900)
        elif number >= 500:
            return "D" + roman(number-500)
        elif number >= 400:
            return "CD" + roman(number-400)
        elif number >= 100:
            return "C" + roman(number-100)
        elif number >= 90:
            return "XC" + roman(number-90)
        elif number >= 50:
            return "L" + roman(number-50)
        elif number >= 40:
            return "XL" + roman(number-40)
        elif number >= 10:
            return "X" + roman(number-10)
        elif number >= 9:
            return "IX" + roman(number-9)
        elif number >= 5:
            return "V" + roman(number-5)
        elif number >= 4:
            return "IV" + roman(number-4)
        elif number >= 1:
            return "I" + roman(number-1)
        else:
            return ""
