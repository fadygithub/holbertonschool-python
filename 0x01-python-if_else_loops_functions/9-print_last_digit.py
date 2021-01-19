#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_digit = (abs(number) % 10)
    else:
        digit = number % 10
    print('{:d}'.format(last_digit), end="")
    return last_digit
