#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    l = sys.argv
    a = int(l[1])
    b = int(l[3])
    le = len(sys.argv) - 1
    if le != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if l[2] != '+' and l[2] != '-' and l[2] != '*' and l[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if l[2] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif l[2] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif l[2] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
