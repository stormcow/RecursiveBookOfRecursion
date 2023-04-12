def quicksort(items, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(items) - 1

    print(f"\nquicksort() calles on this range: {items[left:right + 1]}")
    print(f"............the full list is: {items}")

    if right <= left:
        return

    i = left
    pivotValue = items[right]

    print(f"............The pivos is {pivotValue}")

    for j in range(left, right):
        if items[j] <= pivotValue:
            items[i], items[j] = items[j], items[i]
            i += 1

    items[i], items[right] = items[right], items[i]

    print(f"....After swapping, the range is {items[left:right + 1]}")
    print(f"Recursively calling quicksort on: {items[left:i]}")

    quicksort(items, left, i - 1)
    quicksort(items, i + 1, right)


myList = [0, 7, 6, 3, 1, 2, 5, 4]
quicksort(myList)
print(myList)
