def largest_product(series: str, size: int):
    result = 0

    if size > len(series):
        # span of numbers is longer than number series
        raise ValueError("span must be smaller than string length")

    if size < 0:
        # span of number is negative
        raise ValueError("span must not be negative")

    if not series.isnumeric():
        # series includes non-number input
        raise ValueError("digits input must only contain digits")

    if len(series) == size:
        result = 1
        for number in series:
            result *= int(number)

    sub_strings = []

    for counter in range(len(series)):
        if len(series[counter:counter+size]) == size:
            sub_strings.append(series[counter:counter+size])

    if len(sub_strings)>0:

        for substring in sub_strings:
            substring_result = 1
            for number in substring:
                substring_result *= int(number)

            if substring_result > result:
                result = substring_result

    return result
