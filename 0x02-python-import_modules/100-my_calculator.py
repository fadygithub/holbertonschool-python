#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        sys.stderr.write('Usage: ./100-my_calculator.py <a> <operator> <b>\n')
        exit(1)
    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if str(operator) not in("+", "-", "*", "/"):
        sys.stderr.write('Unknown operator. Available \
        operators: +, -, * and /\n')
        exit(1)
    elif str(operator) == "+":
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    elif str(operator) == "-":
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
    elif str(operator) == "/":
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))
    else:
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
