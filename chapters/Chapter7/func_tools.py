import functools


@functools.lru_cache()
def fibonacci(nthNumber: int) -> int:
    print(f"fibonacci({nthNumber}) called")

    if nthNumber == 1 or nthNumber == 2:
        print(f"Call to fibonacci({nthNumber}) returning 1")
        return 1
    else:
        print(f"Calling fibonacci({nthNumber-1}) (nthNumber - 1)")
        result = fibonacci(nthNumber - 1)

        print(f"Calling fibonacci({nthNumber-2}) (nthNumber - 2)")
        result += fibonacci(nthNumber - 2)

        print(f"Call to fibonacci({nthNumber}) returning {result}")
        return result


print(fibonacci(99))
