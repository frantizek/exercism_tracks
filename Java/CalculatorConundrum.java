import java.util.Objects;

class CalculatorConundrum {
    public String calculate(int operand1, int operand2, String operation) {

        if (Objects.isNull(operation)) {
            throw new IllegalArgumentException("Operation cannot be null");
        } else if ("".equals(operation)){
            throw new IllegalArgumentException("Operation cannot be empty");
        } else if ("+".equals(operation)) {
            return "" + operand1 + " + " + operand2 + " = " + (operand1 + operand2);
        } else if ("*".equals(operation)) {
            return "" + operand1 + " * " + operand2 + " = " + (operand1 * operand2);
        } else if ("/".equals(operation)) {
            if (operand2 == 0) {
                return "" + operand1 + " / " + operand2 + " = undefined";
            } else {
                return "" + operand1 + " / " + operand2 + " = " + (operand1 / operand2);
            }
        } else {
            throw new IllegalOperationException("Operation '" + operation + "' does not exist");
        }
    }
}
