"""Assignment 1: Turtle drawing, QA bot, and simple calculator.

Run on a Linux desktop with: python3 assignment_one_yourname.py
"""

import math
import re
import turtle


# Task A: Turtle drawing
def draw_square(pen, length):
    for _ in range(4):
        pen.forward(length)
        pen.right(90)


def turtle_drawing():
    screen = turtle.Screen()
    screen.setup(width=1100, height=700)
    screen.bgcolor("#101827")

    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.speed(7)  # Keep animation visible while drawing.
    pen.pensize(2)

    colours = ["#ff6b6b", "#ffb86b", "#ffe66d", "#6be3a2",
               "#54d6eb", "#8ba7ff", "#cf94ff"]
    patterns = [(0, draw_square)]

    for pattern_number, (center_x, draw_shape) in enumerate(patterns):
        for layer in range(15):
            length = 25 + layer * 6
            pen.color(colours[(layer + pattern_number) % len(colours)])
            pen.penup()
            pen.goto(center_x, 0)
            pen.setheading(layer * 24)
            pen.pendown()
            draw_shape(pen, length)

    print("Drawing finished. Click the drawing window to continue to the QA bot.", flush=True)
    screen.exitonclick()


# Task B: Keyword QA bot
def qa_bot():
    print("\nAsk me about HKU, robot, Jetson, AI, or human.")
    print("Type 'quit' to finish the bot and start the calculator.\n")

    while True:
        try:
            question = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye!")
            break

        words = set(re.findall(r"[a-z]+", question.lower()))

        if "quit" in words or "exit" in words:
            print("Bot: Goodbye!")
            break
        elif "hku" in words:
            print("Bot: HKU stands for the University of Hong Kong.")
        elif "robot" in words or "robots" in words:
            print("Bot: A robot senses its surroundings and performs actions.")
        elif "jetson" in words:
            print("Bot: Jetson Nano is a small computer for edge AI projects.")
        elif "ai" in words:
            print("Bot: AI helps computers do tasks such as image recognition.")
        elif "human" in words or "humans" in words:
            print("Bot: Humans can learn, reason, and make decisions.")
        else:
            print("Bot: Try asking about HKU, robot, Jetson, AI, or human.")


# Task C: Terminal calculator
def simple_calculator():
    print("\nSimple calculator")
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


def main():
    print("Task A: Turtle drawing", flush=True)
    turtle_drawing()
    print("\nTask B: QA bot")
    qa_bot()
    print("\nTask C: Simple calculator")
    simple_calculator()


if __name__ == "__main__":
    main()
