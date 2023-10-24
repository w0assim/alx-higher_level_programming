#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    match argv[2]:
        case '+':
            print("{} {} {} = {}".format(int(argv[1]), int(argv[2]), int(argv[3]), add(a, b)))
        case '-':
            print("{} {} {} = {}".format(int(argv[1]), int(argv[2]), int(argv[3]), sub(a, b)))
        case '*':
            print("{} {} {} = {}".format(int(argv[1]), int(argv[2]), int(argv[3]), mul(a, b)))
        case '/':
            print("{} {} {} = {}".format(int(argv[1]), int(argv[2]), int(argv[3]), div(a, b)))
        default:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
