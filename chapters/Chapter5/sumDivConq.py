def sumDivConq(array: list[int]):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]

    mid = len(array) // 2

    return sumDivConq(array[0:mid]) + sumDivConq(array[mid:])


myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sumDivConq(myArray))

myArray = [1, 2, 3, 4]
print(sumDivConq(myArray))
