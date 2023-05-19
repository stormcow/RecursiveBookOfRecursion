import turtle

turtle.tracer(10, 0)
turtle.setworldcoordinates(0, 0, 700, 700)
turtle.hideturtle()
turtle.pensize(2)


def drawKochCurve(startPosiion, heading, length):
    if length < 1:
        return
    else:
        recusiveArgs = []
        turtle.penup()
        turtle.goto(startPosiion)
        turtle.setheading(heading)
        recusiveArgs.append(
            {"position": turtle.position(), "heading": turtle.heading()}
        )

        turtle.forward(length / 3)
        turtle.pencolor("white")
        turtle.pendown()
        turtle.forward(length / 3)

        turtle.backward(length / 3)
        turtle.left(60)
        recusiveArgs.append(
            {"position": turtle.position(), "heading": turtle.heading()}
        )

        turtle.pencolor("black")
        turtle.forward(length / 3)
        turtle.right(120)
        recusiveArgs.append(
            {"position": turtle.position(), "heading": turtle.heading()}
        )

        turtle.forward(length / 3)
        turtle.left(60)
        recusiveArgs.append(
            {"position": turtle.position(), "heading": turtle.heading()}
        )

        for i in range(4):
            drawKochCurve(
                recusiveArgs[i]["position"], recusiveArgs[i]["heading"], length / 3
            )
        return


def drawKochSnowflake(startPosition, heading, length):
    turtle.penup()
    turtle.goto(startPosition)
    turtle.setheading(heading)

    for i in range(3):
        curveStartingPosition = turtle.position()
        curveStartingHeading = turtle.heading()
        drawKochCurve(curveStartingPosition, curveStartingHeading, length)

        turtle.penup()
        turtle.goto(curveStartingPosition)
        turtle.setheading(curveStartingHeading)

        turtle.forward(length)
        turtle.right(120)


drawKochSnowflake((100, 500), 0, 500)
turtle.exitonclick()
