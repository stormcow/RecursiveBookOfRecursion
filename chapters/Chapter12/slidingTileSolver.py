import random, time

DIFFICULTY = 40
SIZE = 4
random.seed(1)

BLANK = 0
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"


def displayBoard(board: list[int]) -> None:
    for y in range(SIZE):
        for x in range(SIZE):
            if board[y * SIZE + x] == BLANK:
                print("__ ", end="")
            else:
                print(str(board[y * SIZE + x]).rjust(2) + " ", end="")

        print()


def getNewBoard() -> list[int]:
    board: list[int] = []
    for i in range(1, SIZE * SIZE):
        board.append(i)
    board.append(BLANK)
    return board


def findBlankSpace(board: list[int]) -> list[int]:
    for x in range(SIZE):
        for y in range(SIZE):
            if board[y * SIZE + x] == BLANK:
                return [x, y]
    return [-1, -1]


def makeMove(board: list[int], move: str) -> None:
    bx, by = findBlankSpace(board)

    assert bx > -1
    assert by > -1

    blankIndex = by * SIZE + bx

    if move == UP:
        tileIndex = (by + 1) * SIZE + bx
    elif move == LEFT:
        tileIndex = by * SIZE + (bx + 1)
    elif move == DOWN:
        tileIndex = (by - 1) * SIZE + bx
    elif move == RIGHT:
        tileIndex = by * SIZE + (bx - 1)

    board[blankIndex], board[tileIndex] = board[tileIndex], board[blankIndex]


def undoMove(board: list[int], move: str) -> None:
    if move == UP:
        makeMove(board, DOWN)
    elif move == DOWN:
        makeMove(board, UP)
    elif move == LEFT:
        makeMove(board, RIGHT)
    elif move == RIGHT:
        makeMove(board, LEFT)


def getValidMoves(board: list[int], prevMove: str | None = None) -> list[str]:
    blankx, blanky = findBlankSpace(board)

    assert blankx > -1
    assert blanky > -1

    validMoves: list[str] = []
    if blanky != SIZE - 1 and prevMove != DOWN:
        validMoves.append(UP)
    if blankx != SIZE - 1 and prevMove != RIGHT:
        validMoves.append(LEFT)
    if blanky != 0 and prevMove != UP:
        validMoves.append(DOWN)
    if blankx != 0 and prevMove != LEFT:
        validMoves.append(RIGHT)

    return validMoves


def getNewPuzzle() -> list[int]:
    board = getNewBoard()
    for i in range(DIFFICULTY):
        validMoves = getValidMoves(board)
        makeMove(board, random.choice(validMoves))
    return board


def solve(board: list[int], maxMoves: int) -> bool:
    solutionMoves: list[str] = []
    solved = attemptMove(board, solutionMoves, maxMoves, None)

    if solved:
        displayBoard(board)
        for move in solutionMoves:
            print("Move", move)
            makeMove(board, move)
            print()
            displayBoard(board)
            print()

        print("solved in", len(solutionMoves), "moves:")
        print(", ".join(solutionMoves))
        return True
    else:
        return False


def attemptMove(
    board: list[int], movesMade: list[str], movesRemaining: int, prevMove: str | None
) -> bool:
    if movesRemaining < 0:
        return False
    if board == SOLVED_BOARD:
        return True

    for move in getValidMoves(board, prevMove):
        makeMove(board, move)
        movesMade.append(move)

        if attemptMove(board, movesMade, movesRemaining - 1, move):
            undoMove(board, move)
            return True

        undoMove(board, move)
        movesMade.pop()
    return False


SOLVED_BOARD = getNewBoard()
puzzleBoard = getNewPuzzle()
displayBoard(puzzleBoard)
startTime = time.time()

maxMoves = 10

while True:
    if solve(puzzleBoard, maxMoves):
        break
    maxMoves += 1

print("run in", round(time.time() - startTime, 3), "seconds")
