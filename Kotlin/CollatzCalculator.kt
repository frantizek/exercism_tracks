object CollatzCalculator {
    fun computeStepCount(start: Int): Int {
            var number: Int = start;
            if (number <= 0) {
            throw IllegalArgumentException("Only positive integers are allowed")
            return 0;
            } else {
            var count_steps: Int = 0;
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