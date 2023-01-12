def fibonacci(nthNumber):
    print(f'fibonnaci{nthNumber} called')
    if nthNumber == 1 or nthNumber == 2:
        print(f'call to fibonacci{nthNumber} returning 1')
        return 1
    else:
        print(f'calling fibonacci{nthNumber - 1} and fibonacci{nthNumber - 2}')
        result = fibonacci(nthNumber - 1) + fibonacci(nthNumber - 2)
        print(f'Call to fibonacci{nthNumber} returning {result}')
        return result

print(fibonacci(100))