"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 3
SUPERLIST = 2
EQUAL = 1
UNEQUAL = 0


def is_contiguous_sublist(small, big) -> bool:
    """Return True if small is a contiguous sublist of big."""
    if small == []:
        return True
    if len(big) < len(small):
        return False
    return any(big[index:index + len(small)] == small for index in range(len(big) - len(small) + 1))


def sublist(list_one, list_two) -> int:
    """Return the sublist category based on the lists' relationship."""
    if list_one == list_two:
        return EQUAL
    if len(list_one) < len(list_two) and is_contiguous_sublist(list_one, list_two):
        return SUBLIST
    if len(list_one) > len(list_two) and is_contiguous_sublist(list_two, list_one):
        return SUPERLIST
    return UNEQUAL
