def sumIterative(n: int):
    result = 0
    i = 1
    while i <= n:
        print(f"{result} + {i} == {result + i}")
        result += i
        i += 1
    return result
def sumRecursive(n: int):
    if n == 1:
        return 1
    return n + sumRecursive(n-1)

print(sumRecursive(8))
print(sumIterative(8))