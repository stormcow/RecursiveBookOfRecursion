fibonacciCache: dict[int, int] = {}


def fibonacci(nthNumber: int, indent: int = 0) -> int:
    global fibonacciCache
    indentation: str = "." * indent
    print(f"{indentation}fibonacci({nthNumber}) called")

    if nthNumber in fibonacciCache:
        print(f"{indentation}Returning memoized result: {fibonacciCache[nthNumber]}")
        return fibonacciCache[nthNumber]

    if nthNumber == 1 or nthNumber == 2:
        print(f"{indentation}Base case fibonacci({nthNumber}), returning 1")
        return 1
    else:
        print(f"{indentation}Calling fibonacci({nthNumber-1})")
        result: int = fibonacci(nthNumber - 1, indent + 1)

        print(f"{indentation}Calling fibonacci({nthNumber-2})")
        result: int = result + fibonacci(nthNumber - 2, indent + 1)

        print(f"Call to fibonacci({nthNumber}) returning {result}")
        fibonacciCache[nthNumber] = result
        return result


print(fibonacci(50))
