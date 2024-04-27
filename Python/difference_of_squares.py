def square_of_sum(number: int) -> int:
    amazing_result = 0
    for current_number in range(1, number+1):
        amazing_result += current_number
    return amazing_result*amazing_result


def sum_of_squares(number: int) -> int:
    amazing_result = 0
    for current_number in range(1, number+1):
        amazing_result += current_number*current_number
    return amazing_result


def difference_of_squares(number):
    return square_of_sum(number)-sum_of_squares(number)
