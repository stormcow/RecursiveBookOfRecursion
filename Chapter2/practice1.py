def iterativeSumOfIntegers(n):
    sum = 0
    
    for i in range(1,n+1):
        sum += i
    
    return sum

print(iterativeSumOfIntegers(1))
print(iterativeSumOfIntegers(2))
print(iterativeSumOfIntegers(3))