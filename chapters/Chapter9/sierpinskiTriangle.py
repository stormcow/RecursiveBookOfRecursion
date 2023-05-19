import turtle

turtle.tracer(100, 0)
turtle.setworldcoordinates(0, 0, 700, 700)
turtle.hideturtle()

MIN_SIZE: float = 4


def midPoint(
    startx: float, starty: float, endx: float, endy: float
) -> tuple[float, float]:
    xDiff: float = abs(startx - endx)
    yDiff: float = abs(starty - endy)
    return (min(startx, endx) + (xDiff / 2.0), min(starty, endy) + (yDiff / 2.0))


def isTooSmall(
    ax: float | int,
    ay: float | int,
    bx: float | int,
    by: float | int,
    cx: float | int,
    cy: float | int,
) -> bool:
    width: float = max(ax, bx, cx) - min(ax, bx, cx)
    height: float = max(ay, by, cy) - min(ay, by, cy)
    return width < MIN_SIZE or height < MIN_SIZE


def drawTriangle(
    ax: float | int,
    ay: float | int,
    bx: float | int,
    by: float | int,
    cx: float | int,
    cy: float | int,
) -> None:
    if isTooSmall(ax, ay, bx, by, cx, cy):
        return
    else:
        turtle.penup()
        turtle.goto(ax, ay)
        turtle.pendown()
        turtle.goto(bx, by)
        turtle.goto(cx, cy)
        turtle.goto(ax, ay)
        turtle.penup()

        mid_ab: tuple[float, float] = midPoint(ax, ay, bx, by)
        mid_bc: tuple[float, float] = midPoint(bx, by, cx, cy)
        mid_ca: tuple[float, float] = midPoint(cx, cy, ax, ay)

        drawTriangle(ax, ay, mid_ab[0], mid_ab[1], mid_ca[0], mid_ca[1])
        drawTriangle(mid_ab[0], mid_ab[1], bx, by, mid_bc[0], mid_bc[1])
        drawTriangle(mid_ca[0], mid_ca[1], mid_bc[0], mid_bc[1], cx, cy)


# drawTriangle(50, 50, 350, 650, 650, 50)
drawTriangle(30, 250, 680, 680, 500, 80)

turtle.exitonclick()
