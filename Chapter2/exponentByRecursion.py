def exponentByRecursion(a, n):
    if n == 1:
        return a
    elif n % 2 == 0:
        result = exponentByRecursion(a, n // 2)
        return result * result
    elif n % 2 == 1:
        result = exponentByRecursion(a, n // 2)
        return result * result * a

print(exponentByRecursion(3,1))
print(exponentByRecursion(10,3))
print(exponentByRecursion(17,10))