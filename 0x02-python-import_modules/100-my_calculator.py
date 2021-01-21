#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

def main():
    arguments = sys.argv
    agruments = arguments[1:]

    if len(arguments) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    elif arguments[2] != "+" and arguments[2] != "-" and arguments[2] != "*" and arguments[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        print("**")
        sys.exit(1)
    
    elif arguments[2] == "+":
        print('{} {} {} = {}'.format(arguments[1], arguments[2], arguments[3], format(add(int(arguments[1]), int(arguments[3])))))

    elif arguments[2] == "-":
        print('{} {} {} = {}'.format(arguments[1], arguments[2], arguments[3], format(sub(int(arguments[1]), int(arguments[3])))))

    elif arguments[2] == "*":
        print('{} {} {} = {}'.format(arguments[1], arguments[2], arguments[3], format(mul(int(arguments[1]), int(arguments[3])))))

    elif arguments[2] == "/":
        print('{} {} {} = {}'.format(arguments[1], arguments[2], arguments[3], format(div(int(arguments[1]), int(arguments[3])))))

if __name__ == '__main__':
    main()
