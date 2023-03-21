MAZE = """
#######################################################################
#S#                 #       # #   #     #         #     #   #         #
# ##### ######### # ### ### # # # # ### # # ##### # ### # # ##### # ###
# #   #     #     #     #   # # #   # #   # #       # # # #     # #   #
# # # ##### # ########### ### # ##### ##### ######### # # ##### ### # #
#   #     # # #     #   #   #   #         #       #   #   #   #   # # #
######### # # # ##### # ### # ########### ####### # # ##### ##### ### #
#       # # # #     # #     # #   #   #   #     # # #   #         #   #
# # ##### # # ### # # ####### # # # # # # # ##### ### ### ######### # #
# # #   # # #   # # #     #     #   #   #   #   #   #     #         # #
### # # # # ### # # ##### ####### ########### # ### # ##### ##### ### #
#   # #   # #   # #     #   #     #       #   #     # #     #     #   #
# ### ####### ##### ### ### ####### ##### # ######### ### ### ##### ###
#   #         #     #     #       #   # #   # #     #   # #   # #   # #
### ########### # ####### ####### ### # ##### # # ##### # # ### # ### #
#   #   #       # #     #   #   #     #       # # #     # # #   # #   #
# ### # # ####### # ### ##### # ####### ### ### # # ####### # # # ### #
#     #         #     #       #           #     #           # #      E#
#######################################################################
""".split(
    "\n"
)

EMPTY = " "
START = "S"
EXIT = "E"
PATH = "."

HEIGHT = len(MAZE)
WIDTH = 0

for row in MAZE:  # set WIDTH to the widest rows width
    if len(row) > WIDTH:
        WIDTH = len(row)

# Make each row in the maze a list as wide as the WIDTH
for i in range(len(MAZE)):
    MAZE[i] = list(MAZE[i])
    if len(MAZE[i]) != WIDTH:
        MAZE[i] = [EMPTY] * WIDTH


def printMaze(maze):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(maze[y][x], end=" ")
        print()
    print()


def findStarT(maze):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if maze[y][x] == START:
                return (x, y)


def solveMaze(maze, x=None, y=None, visited=None):
    if x == None or y == None:
        x, y = findStarT(maze)
        maze[y][x] = EMPTY
    if visited == None:
        visited = []
    if maze[y][x] == EXIT:
        return True

    maze[y][x] = PATH
    visited.append(str(x) + "," + str(y))

    # Explore north neighboring point
    if (
        y + 1 < HEIGHT
        and maze[y + 1][x] in (EMPTY, EXIT)
        and str(x) + "," + str(y + 1) not in visited
    ):
        # RECURSIVE CASE
        if solveMaze(maze, x, y + 1, visited):
            return True
    # Explore south
    if (
        y - 1 >= 0
        and maze[y - 1][x] in (EMPTY, EXIT)
        and str(x) + "," + str(y - 1) not in visited
    ):
        # RECURSIVE
        if solveMaze(maze, x, y - 1, visited):
            return True
    # Explore east
    if (
        x + 1 < WIDTH
        and maze[y][x + 1] in (EMPTY, EXIT)
        and str(x + 1) + "," + str(y) not in visited
    ):
        # RECURSIVE
        if solveMaze(maze, x + 1, y, visited):
            return True
    # Explore west
    if (
        x - 1 >= 0
        and maze[y][x - 1] in (EMPTY, EXIT)
        and str(x - 1) + "," + str(y) not in visited
    ):
        # RECURSIVE
        if solveMaze(maze, x - 1, y, visited):
            return True

    maze[y][x] = EMPTY

    return False


printMaze(MAZE)
solveMaze(MAZE)
printMaze(MAZE)
