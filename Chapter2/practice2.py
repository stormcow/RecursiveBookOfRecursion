def recursiveSumOfSeries(n):
    if n == 1:
        return 1
    return n + recursiveSumOfSeries(n-1)

print(recursiveSumOfSeries(1))
print(recursiveSumOfSeries(2))
print(recursiveSumOfSeries(3))