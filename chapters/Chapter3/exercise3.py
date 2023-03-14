from dataclasses import dataclass
from typing import List

@dataclass
class Point():
    x: int
    y: int

string = """
...##########....................................
...#........#....####..................##########
...#........#....#..#...############...#........#
...##########....#..#...#..........#...##.......#
.......#....#....####...#..........#....##......#
.......#....#....#......############.....##.....#
.......######....#........................##....#
.................####........####..........######
"""
array = [[*line] for line in string.split('\n') ]

array.pop()
array.pop(0)

HEIGHT = len(array)
WIDTH = len(array[0])

def floodFill(point: Point, oldChar: str, newChar: str):
    
    if array[point.y][point.x] != oldChar:
        return
    else:
        array[point.y][point.x] = newChar

        if point.y + 1 < HEIGHT and array[point.y + 1][point.x] == oldChar:
            floodFill(Point(point.x, point.y + 1), oldChar, newChar)
        if point.y - 1 >= 0 and array[point.y - 1][point.x] == oldChar:
            floodFill(Point(point.x, point.y - 1), oldChar, newChar)
        if point.x + 1 < WIDTH and array[point.y][point.x + 1] == oldChar:
            floodFill(Point(point.x + 1, point.y), oldChar, newChar)
        if point.x - 1 >= 0 and array[point.y][point.x - 1] == oldChar:
            floodFill(Point(point.x - 1, point.y), oldChar, newChar)
    
count = 0

for y, line in enumerate(array):
    for x, char in enumerate(line):
        if array[y][x] == '.':
            count += 1
            point = Point(x,y)
            floodFill(point, '.', '#')

        
print(count)