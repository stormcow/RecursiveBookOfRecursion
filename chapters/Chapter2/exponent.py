def exponentByIteration(a, n):
    result = 1
    for i in range(n):
        result *= a
    return result


def myExponentByRecursion(a, n):
    if n == 1:
        return a
    return a * myExponentByRecursion(a, n - 1)


def exponentByRecursion(a, n):
    if n == 1:
        return a
    elif n % 2 == 0:
        result = exponentByRecursion(a, n // 2)
        return result * result
    elif n % 2 == 1:
        result = exponentByRecursion(a, n // 2)
        return result * result * a


def exponentWithPowerRule(a, n):
    opStack = []
    while n > 1:
        if n % 2 == 0:
            opStack.append("square")
            n = n // 2
        elif n % 2 == 1:
            n -= 1
            opStack.append("multiply")

    result = a
    while opStack:
        op = opStack.pop()
        if op == "multiply":
            result *= a
        elif op == "square":
            result *= result
    return result


print(myExponentByRecursion(5, 3))
print(exponentByIteration(5, 3))
print(exponentByRecursion(17, 3))
print(exponentWithPowerRule(17,3))
