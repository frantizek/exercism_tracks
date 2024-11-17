class CollatzCalculator {

    int computeStepCount(int start) {
        if (start <= 0) {
            throw new IllegalArgumentException("Only positive integers are allowed");
        } else {
            int count_steps = 0;
            while (start != 1)
                {
                    if (start % 2 == 0) {
                        start = start / 2;
                    }
                    else {
                        start = (start * 3) + 1;
                    }
                    count_steps += 1;
                }
            return count_steps;
        }
    }
}