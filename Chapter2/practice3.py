def iterativeSumOfPowersOf2(n):
    sum = 0
    
    if n == 0:
        return 1
    
    for i in range(1, n + 1):
        sum += 2 ** i
    
    return sum

print(iterativeSumOfPowersOf2(1))
print(iterativeSumOfPowersOf2(2))
print(iterativeSumOfPowersOf2(3))