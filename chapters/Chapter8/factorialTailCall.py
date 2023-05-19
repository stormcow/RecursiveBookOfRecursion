def factorial(number: int, accum: int = 1) -> int:
    if number == 1:
        return accum
    else:
        return factorial(number - 1, accum * number)


print(factorial(5))
