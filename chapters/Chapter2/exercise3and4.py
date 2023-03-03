def sumNthPowersOf2Iterative(n: int):
    result = 0
    while n >= 1:
        result += (2 ** n)
        n -= 1
    return result
def sumNthPowersOf2Recursive(n: int):
    if n == 1:
        return 2
    return (2 ** n) + sumNthPowersOf2Recursive(n-1) 
print(sumNthPowersOf2Iterative(3))
print(sumNthPowersOf2Recursive(3))