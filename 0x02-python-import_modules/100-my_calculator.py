#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    ar = sys.argv
    ar = arguments[1:]

    if len(ar) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    elif ar[2] != "+" and ar[2] != "-" and ar[2] != "*" and ar[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        print("**")
        sys.exit(1)
    
    elif ar[2] == "+":
        print('{} {} {} = {}'.format(ar[1], ar[2], ar[3], format(add(int(ar[1]), int(ar[3])))))

    elif ar[2] == "-":
        print('{} {} {} = {}'.format(ar[1], ar[2], arguments[3], format(sub(int(ar[1]), int(ar[3])))))

    elif ar[2] == "*":
        print('{} {} {} = {}'.format(ar[1], ar[2], arguments[3], format(mul(int(ar[1]), int(ar[3])))))

    elif ar[2] == "/":
        print('{} {} {} = {}'.format(ar[1], ar[2], arguments[3], format(div(int(ar[1]), int(ar[3])))))

if __name__ == '__main__':
    main()
