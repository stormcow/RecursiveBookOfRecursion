import random

WIDTH = 39
HEIGHT = 19

assert WIDTH % 2 == 1 and WIDTH >= 3
assert HEIGHT % 2 == 1 and HEIGHT >= 3

SEED = 1
random.seed(SEED)

EMPTY = " "
MARK = "@"
WALL = chr(9608)
NORTH, SOUTH, EAST, WEST = "n", "s", "e", "w"

maze: dict[tuple[int, int], str] = {}

for x in range(WIDTH):
    for y in range(HEIGHT):
        maze[(x, y)] = WALL


def printMaze(
    maze: dict[tuple[int, int], str], markX: int | None = None, markY: int | None = None
) -> None:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if markX == x and markY == y:
                print(MARK, end="")
            else:
                print(maze[(x, y)], end="")
        print()


def visit(x: int, y: int) -> None:
    maze[(x, y)] = EMPTY
    print(maze, x, y)
    print("\n\n")

    while True:
        unvisitedNeighbors: list[str] = []

        if y > 1 and (x, y - 2) not in hasVisited:
            unvisitedNeighbors.append(NORTH)

        if y < HEIGHT - 2 and (x, y + 2) not in hasVisited:
            unvisitedNeighbors.append(SOUTH)

        if x > 1 and (x - 2, y) not in hasVisited:
            unvisitedNeighbors.append(WEST)

        if x < WIDTH - 2 and (x + 2, y) not in hasVisited:
            unvisitedNeighbors.append(EAST)

        if len(unvisitedNeighbors) == 0:
            return
        else:
            nextIntersection = random.choice(unvisitedNeighbors)

            if nextIntersection == NORTH:
                nextX = x
                nextY = y - 2
                maze[(x, y - 1)] = EMPTY
            elif nextIntersection == SOUTH:
                nextX = x
                nextY = y + 2
                maze[(x, y + 1)] = EMPTY
            elif nextIntersection == WEST:
                nextX = x - 2
                nextY = y
                maze[(x - 1, y)] = EMPTY
            elif nextIntersection == EAST:
                nextX = x + 2
                nextY = y
                maze[(x + 1, y)] = EMPTY

            hasVisited.append((nextX, nextY))
            visit(nextX, nextY)

hasVisited = [(1, 1)]
visit(1,1)
printMaze(maze)
