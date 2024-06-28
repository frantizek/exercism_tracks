def convert(number: int) -> str:
    Pli = "Pling"  # 3
    Pla = "Plang"  # 5
    Plo = "Plong"  # 7

    if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
        return Pli + Pla + Plo
    elif number % 3 == 0 and number % 5 == 0:
        return Pli + Pla
    elif number % 3 == 0 and number % 7 == 0:
        return Pli + Plo
    elif number % 5 == 0 and number % 7 == 0:
        return Pla + Plo
    elif number % 3 == 0:
        return Pli
    elif number % 5 == 0:
        return Pla
    elif number % 7 == 0:
        return Plo
    else:
        return str(number)
