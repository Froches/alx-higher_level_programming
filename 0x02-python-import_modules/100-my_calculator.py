#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if operator == '+':
        result = a + b
    elif operator == '*':
        result = a * b
    elif operator == '-':
        result = a - b
    else:
         if b == 0:
            print("Error: Division by zero is not allowed.")
            sys.exit(1)
            result = a / b

print("{} {} {} = {}".format(a, operator, b, result))
