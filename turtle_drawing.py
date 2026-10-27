"""Task A: Draw colourful square, triangle, and star patterns with Turtle.

Run in a Linux graphical desktop: python3 turtle_drawing.py
"""


def draw_square(pen, length):
    for _ in range(4):
        pen.forward(length)
        pen.right(90)


def draw_triangle(pen, length):
    for _ in range(3):
        pen.forward(length)
        pen.left(120)


def draw_star(pen, length):
    for _ in range(5):
        pen.forward(length)
        pen.right(144)


def main():
    try:
        import turtle

        screen = turtle.Screen()
    except Exception as error:
        print("Turtle needs a Linux graphical desktop and Tkinter.")
        print("Details:", error)
        return

    screen.setup(width=1100, height=700)
    screen.title("Colourful Turtle Patterns")
    screen.bgcolor("#101827")
    screen.tracer(0)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(2)

    colours = [
        "#ff6b6b", "#ffb86b", "#ffe66d", "#6be3a2",
        "#54d6eb", "#8ba7ff", "#cf94ff", "#ff91cd",
    ]
    patterns = [
        ("SQUARE", -315, draw_square),
        ("TRIANGLE", 0, draw_triangle),
        ("STAR", 315, draw_star),
    ]

    pen.penup()
    pen.goto(0, 275)
    pen.color("white")
    pen.write("TURTLE PATTERN GALLERY", align="center", font=("Arial", 24, "bold"))

    for pattern_number, (label, center_x, shape_function) in enumerate(patterns):
        for layer in range(22):
            length = 18 + layer * 5  # Change the side length in each loop.
            colour_index = (layer + pattern_number * 2) % len(colours)
            pen.color(colours[colour_index])  # Change the colour in each loop.

            pen.penup()
            pen.goto(center_x, 0)
            pen.setheading(layer * 25)
            pen.pendown()
            shape_function(pen, length)

        pen.penup()
        pen.goto(center_x, -235)
        pen.color("white")
        pen.write(label, align="center", font=("Arial", 16, "bold"))

    pen.goto(0, -305)
    pen.color("#b8c8df")
    pen.write("Click the window to close it", align="center", font=("Arial", 12, "normal"))
    screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()
