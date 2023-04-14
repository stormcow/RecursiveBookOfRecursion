import random
import time

BIG_ARRAY = [random.randint(0, 1_000_000) for x in range(0, 1_000_00)]


def linearSearch(array: list[int], needle: int):
    for index, value in enumerate(array):
        if value == needle:
            return index
    return False


def quickSort(array: list[int], left: int = None, right: int = None):
    if left == None:
        left = 0
    if right == None:
        right = len(array) - 1

    if left >= right:
        return

    i = left
    pivot = array[right]

    for j in range(left, right):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[i], array[right] = array[right], array[i]

    quickSort(array, left, i - 1)
    quickSort(array, i + 1, right)


def binarySearch(array: list[int], needle: int, left: int = None, right: int = None):
    if left == None:
        left = 0
    if right == None:
        right = len(array) - 1

    if left > right:
        return None

    mid = (left + right) // 2

    if needle == array[mid]:
        return mid
    elif needle < array[mid]:
        return binarySearch(array, needle, left, mid - 1)
    elif needle > array[mid]:
        return binarySearch(array, needle, mid + 1, right)


startTime = time.time()
for _ in range(100000):
    linearSearch(BIG_ARRAY, random.randint(0, 1_000_000))
endTime = time.time() - startTime
print(f"{endTime} seconds for linear search 10 000 times")

startTime = time.time()
quickSort(BIG_ARRAY)
for _ in range(100000):
    binarySearch(BIG_ARRAY, random.randint(0, 1_000_000))
endTime = time.time() - startTime
print(f"{endTime} seconds for sort and search the array 10 000 times")
