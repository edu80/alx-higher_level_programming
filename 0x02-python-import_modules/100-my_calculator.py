#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    op = ['+', '/', '-', '*']
    n = len(argv)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    first = int(argv[1])
    operator = argv[2]
    second = int(argv[3])
    if operator == '+':
        print(f"{first} {operator} {second} = {add(first, second)}")
    elif operator == '*':
        print(f"{first} {operator} {second} = {mul(first, second)}")
    elif operator == '/':
        print(f"{first} {operator} {second} = {div(first, second)}")
    else:
        print(f"{first} {operator} {second} = {sub(first, second)}")
