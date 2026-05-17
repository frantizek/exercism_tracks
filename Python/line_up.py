"""
Given a name and a number,
your task is to produce a sentence using that name and that number as an ordinal numeral.
Yaʻqūb expects to use numbers from 1 up to 999.

Rules:
Numbers ending in 1 (unless ending in 11) → "st"
Numbers ending in 2 (unless ending in 12) → "nd"
Numbers ending in 3 (unless ending in 13) → "rd"
All other numbers → "th"
"""

def line_up(name: str, number: int) -> str:
    """ Produce a sentence using that name and that number as an ordinal numeral. """

    # Just in case the number is not sent to me as string, cast it anyway
    str_number = str(number)


    if str_number.endswith("1") and not str_number.endswith("11"):
        str_number += "st"
    elif str_number.endswith("2") and not str_number.endswith("12"):
        str_number += "nd"
    elif str_number.endswith("3") and not str_number.endswith("13"):
        str_number += "rd"
    else:
        str_number += "th"

    return f"{name}, you are the {str_number} customer we serve today. Thank you!"