"""Turtle Scene Exercise."""

__author__ = "730392257"

from turtle import Turtle, colormode, done

colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    night: Turtle = Turtle()
    
    draw_square(night, -360, 360, 720)
    
    #  draws stars
    i: int = 0
    while i < 150:
        from random import randint
        placement_x: int = randint(-350, 350)
        placement_y: int = randint(0, 490)
        draw_star(night, placement_x, placement_y)
        i += 1
    draw_moon(night, 240, 200)
    draw_tree(night, -330, -200)

    done()


def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square that represents the night sky."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.speed(0)
    a_turtle.color(25, 55, 120)
    i: int = 0
    a_turtle.begin_fill()
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i += 1
    a_turtle.end_fill()


def draw_star(star: Turtle, x: float, y: float) -> None:
    """Draws small stars in the sky. The call for this function in main attempts to use the randint function to randomize where the stars are placed in the sky."""
    star.penup()
    star.goto(x, y)
    star.pendown()
    star.color(239, 234, 190)
    star.speed(0)
    star.begin_fill()
    star.circle(2)
    star.end_fill()
    star.hideturtle()


def draw_moon(moon: Turtle, x: float, y: float) -> None:
    """Draws a bright white moon in the top right corner. This procedure used the circle function."""
    moon.penup()
    moon.goto(x, y)
    moon.pendown()
    moon.color("white")
    moon.speed(0)
    moon.begin_fill()
    moon.circle(40)
    moon.end_fill()
    moon.hideturtle()


def draw_tree_base(tree_base: Turtle, x: float, y: float) -> None:
    """Draws the base of the trees."""
    tree_base.penup()
    tree_base.goto(x, y)
    tree_base.pendown()
    tree_base.speed(0)
    tree_base.color(85, 59, 44)
    tree_base.begin_fill()
    i: int = 0
    while i < 4:
        if i % 2 == 0:
            tree_base.forward(40)
        else:
            tree_base.forward(150)
        tree_base.right(90)
        i += 1
    tree_base.end_fill()


def draw_tree_top(tree_top: Turtle, x: float, y: float) -> None:
    """Draws tops of the trees."""
    tree_top.penup()
    tree_top.goto(x, y)
    tree_top.pendown()
    tree_top.speed(0)
    tree_top.color(42, 94, 16)
    tree_top.begin_fill()
    i: int = 0
    while i < 3:
        tree_top.forward(100)
        tree_top.left(120)
        i += 1
    tree_top.end_fill()


def draw_tree(tree: Turtle, x: float, y: float) -> None:
    #  draws tree bases
    i = 0
    # x = -330
    # y = -200
    while i < 7:
        draw_tree_base(tree, x, y)
        x += 100
        i += 1
    #  draws tops of trees
    i = 0
    x = -360
    y = -200
    z: int = 1
    while i < 7:
        while z <= 3:
            draw_tree_top(tree, x, y)
            y += 50
            z += 1
        x += 100
        i += 1
        y -= 150
        z -= 3


if __name__ == "__main__":
    main()