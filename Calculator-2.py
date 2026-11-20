import math
import operator


def exponentiation(num1, num2):
    return math.pow(num1, num2)


def square_root(num1, _num2):
    return math.sqrt(num1)


def logarithm(num1, _num2):
    return math.log(num1)


class Calculator:
    def __init__(self):
        self.init()

    def init(self):
        self.operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }

    def add_operation(self, symbol, function):
        self.operations[symbol] = function

    def calculate(self, num1, operation, num2):
        if (
            not isinstance(num1, (int, float))
            or isinstance(num1, bool)
            or not isinstance(num2, (int, float))
            or isinstance(num2, bool)
        ):
            message = "Both values must be numbers."
            print(f"Error: {message}")
            raise TypeError(message)

        if not isinstance(operation, str) or operation not in self.operations:
            message = f"Invalid operation: {operation}"
            print(f"Error: {message}")
            raise ValueError(message)

        try:
            return self.operations[operation](num1, num2)
        except (OverflowError, ValueError, ZeroDivisionError) as error:
            print(f"Error: {error}")
            raise


def main():
    calculator = Calculator()
    calculator.add_operation("**", exponentiation)
    calculator.add_operation("sqrt", square_root)
    calculator.add_operation("log", logarithm)

    print("Available operations: +, -, *, /, **, sqrt, log")
    print("For sqrt and log, the second number is ignored.")

    while True:
        first_input = input("Enter the first number (or q to quit): ").strip()
        if first_input.lower() == "q":
            print("Goodbye!")
            break

        operation = input("Enter the operation: ").strip()
        second_input = input("Enter the second number: ").strip()

        try:
            num1 = float(first_input)
            num2 = float(second_input)
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue

        try:
            result = calculator.calculate(num1, operation, num2)
        except (OverflowError, TypeError, ValueError, ZeroDivisionError):
            continue

        print(f"The result is: {result:g}")


if __name__ == "__main__":
    main()