# The ISBN-10 verification process is used to validate book identification numbers.
# These normally contain dashes and look like: 3-598-21508-8
# The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only).
# In the case the check character is an X, this represents the value '10'.
# These may be communicated with or without hyphens, and can be checked for their validity by the following formula:
# (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
# If the result is 0, then it is a valid ISBN-10, otherwise it is invalid.
from itertools import accumulate


def is_valid(isbn: str) -> bool:
    # clean the string from hyphens
    isbn_without_hyphens = str(isbn.replace("-", "")).upper()
    if len(isbn_without_hyphens) != 10:
        return False
    # now, the remaining characters must be valid
    for character in isbn_without_hyphens:
        if character in "0123456789X":
            continue
        else:
            return False

    accumulate_result = 0
    from_10_to_one = 10
    for number in isbn_without_hyphens:
        if number == "X" and from_10_to_one != 1:
            return False
        elif number == "X" and from_10_to_one == 1:
            accumulate_result += 10 * from_10_to_one
        else:
            accumulate_result += int(number) * from_10_to_one
        from_10_to_one -= 1
    if accumulate_result%11 != 0:
        return False
    return True
