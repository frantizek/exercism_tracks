# The Greek mathematician Nicomachus devised a classification scheme for positive integers,
# identifying each as belonging uniquely to the categories of perfect, abundant, or deficient
# based on their aliquot sum.
# The aliquot sum is defined as the sum of the factors of a number not including the number itself.
# For example, the aliquot sum of 15 is 1 + 3 + 5 = 9.

def extract_factors(number:int) -> list[int]:
    factors = []
    if number<=0:
        return factors
    else:
        for possible_factor in range(1, number):
            if number%possible_factor == 0:
                factors.append(possible_factor)
    return factors


def classify(number:int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        # if a number to be classified is less than 1.
        raise ValueError("Classification is only possible for positive integers.")
    factors = extract_factors(number)
    sum_factors = sum(factors)
    if sum_factors == number:
        return "perfect"
    elif sum_factors < number:
        return "deficient"
    else:
        return "abundant"
