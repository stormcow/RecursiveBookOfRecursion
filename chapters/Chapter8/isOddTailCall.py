def isOdd(number: int) -> bool:
    if number == 0:
        return False
    else:
        return not isOdd(number - 1)


def isOddTailCaill(number: int, inversionAccum: bool = False) -> bool:
    if number == 0:
        return inversionAccum
    else:
        return isOddTailCaill(number - 1, not inversionAccum)
