# Your task is to implement a binary search algorithm.

# A binary search algorithm finds an item in a list by repeatedly splitting it in half,
# only keeping the half which contains the item we're looking for.
# It allows us to quickly narrow down the possible locations of our item until we find it,
# or until we've eliminated all possible locations.
#


def find(search_list: list[int], value: int) -> int:
    # The algorithm looks like this:
    position = -1
    first = 0
    last = len(search_list) - 1
    # Otherwise, repeat the process on the part of the list that has not been eliminated.
    while (first <= last) and (position == -1):
        # Find the middle element of a sorted list and compare it with the item we're looking for.
        middle = (first + last) // 2
        # If the middle element is our item, then we're done!
        if search_list[middle] == value:
            position = middle
        else:
            # If the middle element is less than our item,
            # we can eliminate that element and all the elements before it.
            if value < search_list[middle]:
                last = middle - 1
            # If the middle element is greater than our item,
            # we can eliminate that element and all the elements after it.
            else:
                first = middle + 1
    if position != -1:
        return position
    else:
        # If every element of the list has been eliminated then the item is not in the list.
        raise ValueError("value not in array")
