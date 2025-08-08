import java.util.Objects;

class CalculatorConundrum {
    public String calculate(int operand1, int operand2, String operation) {

        if (Objects.isNull(operation)) {
            throw new IllegalArgumentException("Operation cannot be null");
        } else if ("".equals(operation)){
            throw new IllegalArgumentException("Operation cannot be empty");
        } else if ("+".equals(operation)) {
            return String.format("%d + %d = %d", operand1, operand2, operand1 + operand2);
        } else if ("*".equals(operation)) {
            return String.format("%d * %d = %d", operand1, operand2, operand1 * operand2);
        } else if ("/".equals(operation)) {

            try {
                return String.format("%d / %d = %d", operand1, operand2, operand1 / operand2);
            } catch (ArithmeticException e) {
                throw new IllegalOperationException("Division by zero is not allowed", e);
            }

        } else {
            throw new IllegalOperationException("Operation '" + operation + "' does not exist");
        }
    }
}
