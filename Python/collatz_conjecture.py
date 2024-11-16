def steps(number: int) -> int:
    if number <= 0:
        # example when argument is zero or a negative integer
        raise ValueError("Only positive integers are allowed")
        return 0
    else:
        # Take any positive integer n 
        count_steps = 0
        # Repeat the process indefinitely
        while number != 1:
            # If n is even 
            if number % 2 == 0:
                # divide n by 2 to get n / 2
                number = number / 2
            # If n is odd
            else:
                # multiply n by 3 and add 1 to get 3n + 1
                number = (number * 3) + 1
            count_steps += 1
        # return the number of steps required to reach 1
        return count_steps