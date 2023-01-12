def recursiveSumPowersOf2(n):
    if n == 1:
        return 2
    
    return (2 ** n) + recursiveSumPowersOf2(n-1)

print(recursiveSumPowersOf2(2))
print(recursiveSumPowersOf2(3))
print(recursiveSumPowersOf2(4))