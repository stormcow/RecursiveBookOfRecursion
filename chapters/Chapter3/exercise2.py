from typing import List

def product(array: List[int]):
    if len(array) == 0:
        return 1
    return array[0] * product(array[1:])

nums = [1,2,3,4]
print(product(nums))