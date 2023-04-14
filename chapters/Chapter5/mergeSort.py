def mergeSort(items):
    print(".....mergeSort() called on:", items)

    # BASE CASE - Zero or one item is naturally sorted:
    if len(items) < 2:
        return items

    # RECURSIVE CASE - Pass the left and right halves to mergeSort():
    # Round down if items doesn't divide in half evenly:
    mid = len(items) // 2

    left = mergeSort(items[:mid])
    right = mergeSort(items[mid:])

    # BASE CASE - Returned merged, sorted data:
    # At this point, left should be sorted and right should be
    # sorted. We can merge them into a single sorted list.
    sorted = []
    iLeft = 0
    iRight = 0
    while len(sorted) < len(items):
        # Append the smaller value to sortedResult.
        if left[iLeft] < right[iRight]:
            sorted.append(left[iLeft])
            iLeft += 1
        else:
            sorted.append(right[iRight])
            iRight += 1

        # If one of the pointers has reached the end of its list,
        # put the rest of the other list into sortedResult.
        if iLeft == len(left):
            sorted.extend(right[iRight:])
            break
        elif iRight == len(right):
            sorted.extend(left[iLeft:])
            break

    print("The two halves merged into:", sorted)

    return sorted  # Returns a sorted version of items.


myList = [
    2.7,
    31,
    431,
    31,
    12,
    233,
    41,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    4,
    3,
    11,
    22,
    3,
    45,
    64,
    2,
]
myList = mergeSort(myList)
print(myList)
