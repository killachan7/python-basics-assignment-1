import turtle


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
    screen = turtle.Screen()
    screen.setup(width=1100, height=700)
    screen.bgcolor("#101827")

    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.speed(7)
    pen.pensize(2)

    colours = ["#ff6b6b", "#ffb86b", "#ffe66d", "#6be3a2", "#54d6eb", "#8ba7ff", "#cf94ff"]
    patterns = [(-315, draw_square), (0, draw_triangle), (315, draw_star)]

    for pattern_number, (center_x, draw_shape) in enumerate(patterns):
        for layer in range(15):
            length = 25 + layer * 6
            pen.color(colours[(layer + pattern_number) % len(colours)])
            pen.penup()
            pen.goto(center_x, 0)
            pen.setheading(layer * 24)
            pen.pendown()
            draw_shape(pen, length)

    screen.exitonclick()


if __name__ == "__main__":
    main()
