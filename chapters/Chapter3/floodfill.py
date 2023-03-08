from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


area = [
    ["1", "1", "1", "2", "1", "1", "1"],
    ["1", "1", "2", "1", "2", "1", "1"],
    ["1", "2", "1", "1", "1", "2", "1"],
    ["2", "1", "1", "1", "1", "1", "2"],
    ["1", "2", "1", "1", "1", "2", "1"],
    ["1", "1", "2", "1", "2", "1", "1"],
    ["1", "1", "1", "2", "1", "1", "1"],
]

HEIGH = len(area)
WIDTH = len(area[0])


# old char, new char
def myFill(point: Point, oldChar: str, newChar: str):
    printArea()
    if area[point.y][point.x] != oldChar:
        return
    else:
        area[point.y][point.x] = newChar

        if point.y + 1 < HEIGH and area[point.y + 1][point.x] == oldChar:
            myFill(Point(point.x, point.y + 1), oldChar, newChar)
        if point.y - 1 >= 0 and area[point.y - 1][point.x] == oldChar:
            myFill(Point(point.x, point.y - 1), oldChar, newChar)
        if point.x + 1 < WIDTH and area[point.y][point.x + 1] == oldChar:
            myFill(Point(point.x + 1, point.y), oldChar, newChar)
        if point.x - 1 >= 0 and area[point.y][point.x - 1] == oldChar:
            myFill(Point(point.x - 1, point.y), oldChar, newChar)


def printArea():
    for line in area:
        string = ''
        for char in line:
            string+= char
        print(string)
    endStr = '*' * WIDTH
    print(endStr)

printArea()
myFill(Point(3,3),'1','O')
printArea()