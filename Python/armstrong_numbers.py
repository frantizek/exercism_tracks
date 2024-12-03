def is_armstrong_number(number):
    if number < 0:
        number = abs(number)
    amount_of_digits = len(str(number))
    number_as_string = str(number)
    sum_of_its_own_digits = 0
    for digit in number_as_string:
        sum_of_its_own_digits += int(digit)**amount_of_digits
    return number == sum_of_its_own_digits