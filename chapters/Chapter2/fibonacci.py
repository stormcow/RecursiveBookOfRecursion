def fibonacciByIteration(nthNumber):
    a, b = 1, 1
    print(f"a = {a}, b = {b}")
    for i in range(1, nthNumber):
        a, b = b, a + b
        print(f"a = {a}, b = {b}")
    return a

def fibonacciByRecursion(nthNumber):
    print(f"fibonacci({nthNumber}) called")
    if nthNumber ==1 or nthNumber ==2:
        print(f"call to fibonacci({nthNumber}) returning 1")
        return 1
    else:
        print(f"calling fibonacci({nthNumber-1}) and fibonacci({nthNumber-2})")
        result = fibonacciByRecursion(nthNumber - 1) + fibonacciByRecursion(nthNumber - 2)
        print(f"call to fibonacci({nthNumber}) returning")
        return result


print(fibonacciByIteration(10))
print(fibonacciByRecursion(10))