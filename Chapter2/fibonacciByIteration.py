def fibonacci(nthNumber):
    a, b = 1, 1
    print(f'a = {a}, b = {b}')
    for i in range(1, nthNumber):
        a, b = b, a+b
        print(f'a = {a}, b = {b}')
    return a

print(fibonacci(10))