from typing import List
def myRecursiveSum(array: List):
    if len(array) == 1:
        return array[0]
    elif len(array) == 0:
        return 0 
    else:
        return array[0] + myRecursiveSum(array[1:])

def booksRecursiveSum(numbers: List):
    if len(numbers) == 0:
        return 0
    else:
        head = numbers[0]
        tail = numbers[1:]
        return head + booksRecursiveSum(tail)

print(myRecursiveSum([5,2,4,8]))
print(booksRecursiveSum([5,2,4,8]))