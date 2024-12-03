using System;

public static class CollatzConjecture
{
    public static int Steps(int number)
    {
        if (number <= 0) {
            throw new ArgumentOutOfRangeException("Only positive integers are allowed");
            return 0;
            } else {
            int count_steps = 0;
            while (number != 1)
                {
                    if (number % 2 == 0) {
                        number = number / 2;
                        }
                    else {
                        number = (number * 3) + 1;
                        }
                    count_steps += 1;
                    }
            return count_steps;
        }
    }
}