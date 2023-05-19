import turtle

turtle.tracer(10, 0)
turtle.setworldcoordinates(0, 0, 700, 700)
turtle.hideturtle()

LINE_LENGTH = 0.8
ANGLE = 88
LEVELS = 8
DRAW_SOLID = False


def hilberCurveQuadrant(level, angle):
    if level == 0:
        return
    else:
        turtle.right(angle)
        hilberCurveQuadrant(level - 1, -angle)
        turtle.forward(LINE_LENGTH)
        turtle.left(angle)
        hilberCurveQuadrant(level - 1, angle)
        turtle.forward(LINE_LENGTH)
        hilberCurveQuadrant(level - 1, angle)
        turtle.left(angle)
        turtle.forward(LINE_LENGTH)
        hilberCurveQuadrant(level - 1, -angle)
        turtle.right(angle)
        return


def hilbertCurve(startingPosition):
    turtle.penup()
    turtle.goto(startingPosition)
    turtle.pendown()
    if DRAW_SOLID:
        turtle.begin_fill()
    hilberCurveQuadrant(LEVELS, ANGLE)
    turtle.forward(LINE_LENGTH)

    hilberCurveQuadrant(LEVELS, ANGLE)
    turtle.left(ANGLE)
    turtle.forward(LINE_LENGTH)
    turtle.left(ANGLE)

    hilberCurveQuadrant(LEVELS, ANGLE)
    turtle.forward(LINE_LENGTH)

    hilberCurveQuadrant(LEVELS, ANGLE)
    turtle.left(ANGLE)
    turtle.forward(LINE_LENGTH)
    turtle.left(ANGLE)
    if DRAW_SOLID:
        turtle.end_fill()


hilbertCurve((50, 650))
turtle.exitonclick()
