#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
import sys


if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")  
sys.exit(1)

operator = {'+': add, '-':sub, '*':mul, '/':div}
operator = sys.agrv[2]

if sys.agrv[2] != {add, sub, mul, div}:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])

print("{} {} {}= {}".format(a, operator, b, (a, b)))
