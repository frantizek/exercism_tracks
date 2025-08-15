def square_root(number):
    if not isinstance(number, int):
        raise TypeError("Expected integer.")
    if number <= 0:
        raise ValueError("Only positive integers allowed.")
    left, right = 1, number
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == number:
            return mid
        elif mid * mid < number:
            left = mid + 1
        else:
            right = mid - 1
    return None