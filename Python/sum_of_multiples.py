def sum_of_multiples(level: int, base_values: list[int]) -> int:

    """
        Your task is to write the code that calculates the energy points that get awarded to players when they complete a level.

        The points awarded depend on two things:

        The level (a number) that the player completed.
        The base value of each magical item collected by the player during that level.
        The energy points are awarded according to the following rules:

        For each magical item, take the base value and find all the multiples of that value that are less than the level number.
        Combine the sets of numbers.
        Remove any duplicates.
        Calculate the sum of all the numbers that are left.
    """

    if level <= 0 or not base_values:
        return 0

    multiples = set()

    for number in base_values:
        if number <= 0:
            # without this, we are probably gonna hit a infinite loop
            continue

        multiple = number
        while multiple < level:
            multiples.add(multiple)
            multiple += number
    return sum(set(multiples))
