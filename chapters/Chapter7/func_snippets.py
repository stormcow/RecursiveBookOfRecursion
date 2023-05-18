def subtract(number1: int | float, number2: int | float) -> int | float:
    return number1 - number2


print(subtract(1, 2.5))

# func with side effects

TOTAL = 0


def addToTotal(amount):
    global TOTAL
    TOTAL += amount
    return TOTAL


addToTotal(10)
addToTotal(10)
