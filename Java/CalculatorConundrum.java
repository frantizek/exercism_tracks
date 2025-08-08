class CalculatorConundrum {
    public String calculate(int operand1, int operand2, String operation) {
        if (operation == "+") {
            return "" + operand1 + " + " + operand2 + " = " + (operand1 + operand2);
        } else if (operation == "*") {
            return "" + operand1 + " * " + operand2 + " = " + (operand1 * operand2);
        } else if (operation == "/") {
            return "" + operand1 + " / " + operand2 + " = " + (operand1 / operand2);
        } else {
            return "";
        }
    }
}
