import time

MULT_TABLE = {(i, j): i * j for i in range(10) for j in range(10)}
BIGGER_TABLE = {(i, j): i * j for i in range(999) for j in range(999)}


# print(MULT_TABLE)


def padZeros(numberString: str, numZeros: int, insertSide: str):
    if insertSide == "left":
        return "0" * numZeros + numberString
    elif insertSide == "right":
        return numberString + "0" * numZeros


def karatsuba(x: int, y: int):
    assert isinstance(x, int), "x must be an int"
    assert isinstance(y, int), "y must be an int"
    x = str(x)
    y = str(y)

    if len(x) == 1 and len(y) == 1:
        # print(f"Lookup {x} * {y} = {BIGGER_TABLE[(int(x),int(y))]}")
        return BIGGER_TABLE[(int(x), int(y))]
        # print(f"Lookup {x} * {y} = {MULT_TABLE[(int(x),int(y))]}")
        # return MULT_TABLE[(int(x), int(y))]

    # print(f"Multiplying {x} * {y}")

    if len(x) < len(y):
        x = padZeros(x, len(y) - len(x), "left")
    elif len(y) < len(x):
        y = padZeros(y, len(x) - len(y), "left")

    halfOfDigits = len(x) // 2

    a = int(x[:halfOfDigits])
    b = int(x[halfOfDigits:])
    c = int(y[:halfOfDigits])
    d = int(y[halfOfDigits:])

    step1Result = karatsuba(a, c)
    step2Result = karatsuba(b, d)
    step3Result = karatsuba(a + b, c + d)

    step4Result = step3Result - step2Result - step1Result

    step1Padding = (len(x) - halfOfDigits) * 2
    step1PaddedNum = int(padZeros(str(step1Result), step1Padding, "right"))

    step4Padding = len(x) - halfOfDigits
    step4PaddedNum = int(padZeros(str(step4Result), step4Padding, "right"))

    # print(f"Solved x, {x}, y, {y} = {step1PaddedNum + step2Result + step4PaddedNum}")

    return step1PaddedNum + step2Result + step4PaddedNum


# print(f"1357 * 2468 = {karatsuba(1357,2468)}")

startTime = time.time()
for i in range(1000000):
    karatsuba(12345678, 87654321)
endTime = time.time() - startTime

print(f"calculation took {endTime} seconds")
