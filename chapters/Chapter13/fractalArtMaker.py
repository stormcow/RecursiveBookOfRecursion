import turtle, math
from typing import Callable

DRAW_FRACTAL = 1

turtle.tracer(5000, 0)
turtle.hideturtle()


def drawFilledSquare(size: float, depth: int) -> None:
    size = int(size)

    turtle.penup()
    turtle.forward(size // 2)
    turtle.left(90)
    turtle.forward(size // 2)
    turtle.left(180)
    turtle.pendown()

    if depth % 2 == 0:
        turtle.pencolor("black")
        turtle.fillcolor("white")
    else:
        turtle.pencolor("black")
        turtle.fillcolor("gray")

    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()


def drawTriangleOutline(size: float, depth: int) -> None:
    size = int(size)

    height = size * math.sqrt(3) / 2
    turtle.penup()
    turtle.left(90)
    turtle.forward(height * (2 / 3))
    turtle.right(150)
    turtle.pendown()

    for i in range(3):
        turtle.forward(size)
        turtle.right(120)


def drawFractal(
    shapeDrawFunction: Callable[[float, int], None],
    size: float,
    specs: list[dict[str, float]],
    maxDepth: int = 8,
    depth: int = 0,
) -> None:
    if depth > maxDepth or size < 1:
        return

    initialX = turtle.xcor()
    initialY = turtle.ycor()
    initialHeading = turtle.heading()

    turtle.pendown()
    shapeDrawFunction(size, depth)
    turtle.penup()

    for spec in specs:
        sizeCh = spec.get("sizeChange", 1.0)
        xCh = spec.get("xChange", 0.0)
        yCh = spec.get("yChange", 0.0)
        angleCh = spec.get("angleChange", 0.0)

        turtle.goto(initialX, initialY)
        turtle.setheading(initialHeading + angleCh)
        turtle.forward(size * xCh)
        turtle.left(90)
        turtle.forward(size * yCh)
        turtle.right(90)

        drawFractal(shapeDrawFunction, size * sizeCh, specs, maxDepth, depth + 1)


if DRAW_FRACTAL == 1:
    drawFractal(
        drawFilledSquare,
        350,
        [
            {"sizeChange": 0.5, "xChange": -0.5, "yChange": 0.5},
            {"sizeChange": 0.5, "xChange": 0.5, "yChange": 0.5},
            {"sizeChange": 0.5, "xChange": -0.5, "yChange": -0.5},
            {"sizeChange": 0.5, "xChange": 0.5, "yChange": -0.5},
        ],
        5,
    )
elif DRAW_FRACTAL == 2:
    drawFractal(drawFilledSquare, 600, [{"sizeChange": 0.95, "angleChange": 7}], 50)
elif DRAW_FRACTAL == 3:
    drawFractal(
        drawFilledSquare,
        600,
        [
            {"sizeChange": 0.8, "yChange": 0.1, "angleChange": -10},
            {"sizeChange": 0.8, "yChange": -0.1, "angleChange": 10},
        ],
    )
elif DRAW_FRACTAL == 4:
    drawFractal(drawTriangleOutline, 20, [{"sizeChange": 1.05, "angleChange": 7}], 80)
elif DRAW_FRACTAL == 5:
    third = 1 / 3
    drawFractal(
        drawFilledSquare,
        600,
        [
            {"sizeChange": third, "yChange": third},
            {"sizeChange": third, "xChange": third},
            {"sizeChange": third, "xChange": third, "yChange": -third},
            {"sizeChange": third, "yChange": -third},
            {"sizeChange": third, "xChange": -third, "yChange": -third},
        ],
    )
elif DRAW_FRACTAL == 6:
    toMid = math.sqrt(3) / 6
    drawFractal(
        drawTriangleOutline,
        600,
        [
            {"sizeChange": 0.5, "yChange": toMid, "angleChange": 0},
            {"sizeChange": 0.5, "yChange": toMid, "angleChange": 120},
            {"sizeChange": 0.5, "yChange": toMid, "angleChange": 240},
        ],
    )
elif DRAW_FRACTAL == 7:
    drawFractal(
        drawTriangleOutline,
        280,
        [
            {"sizeChange": 0.5, "xChange": -0.5, "yChange": 0.5},
            {"sizeChange": 0.3, "xChange": 0.5, "yChange": 0.5},
            {"sizeChange": 0.5, "yChange": -0.7, "angleChange": 15},
        ],
    )
elif DRAW_FRACTAL == 8:
    drawFractal(
        drawFilledSquare,
        100,
        [{"sizeChange": 0.96, "yChange": 0.5, "angleChange": 11}],
        100,
    )
elif DRAW_FRACTAL == 9:
    drawFractal(
        drawFilledSquare,
        200,
        [
            {
                "xChange": math.cos(0 * math.pi / 180),
                "yChange": math.sin(0 * math.pi / 180),
                "sizeChange": 0.4,
            },
            {
                "xChange": math.cos(72 * math.pi / 180),
                "yChange": math.sin(72 * math.pi / 180),
                "sizeChange": 0.4,
            },
            {
                "xChange": math.cos(144 * math.pi / 180),
                "yChange": math.sin(144 * math.pi / 180),
                "sizeChange": 0.4,
            },
            {
                "xChange": math.cos(216 * math.pi / 180),
                "yChange": math.sin(216 * math.pi / 180),
                "sizeChange": 0.4,
            },
            {
                "xChange": math.cos(288 * math.pi / 180),
                "yChange": math.sin(288 * math.pi / 180),
                "sizeChange": 0.4,
            },
        ],
    )
elif DRAW_FRACTAL == 10:
    turtle.tracer(1, 0)
    drawFilledSquare(400, 0)
elif DRAW_FRACTAL == 11:
    turtle.tracer(1, 0)
    drawTriangleOutline(400, 0)
else:
    assert False, "set DRAW_FRACTAL to a number from 1 to 11"

turtle.exitonclick()
