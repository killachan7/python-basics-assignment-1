"""Task C (optional): A terminal calculator for +, -, *, and /.

Run on Linux: python3 simple_calculator.py
"""

import math


def main():
    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.")
        return

    if not math.isfinite(first) or not math.isfinite(second):
        print("Please enter finite numbers.")
        return

    try:
        operator = input("Choose an operator (+, -, *, /): ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.")
        return

    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        if second == 0:
            print("Cannot divide by zero.")
            return
        result = first / second
    else:
        print("Unknown operator. Please choose +, -, *, or /.")
        return

    print(f"Result: {first:g} {operator} {second:g} = {result:g}")


if __name__ == "__main__":
    main()
