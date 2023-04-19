def getCombos(array: list, k: int) -> list:
    if k == 0:
        return []
    elif len(array) == 1:
        return array

    combinations = []
    head = array[:1]
    tail = array[1:]
    tailCombos = getCombos(tail, k - 1)
    for tailCombo in tailCombos:
        newElemenet = [head[0], tailCombo]
        combinations.append(newElemenet)

    combinations.extend(getCombos(tail, k))

    return combinations


print(getCombos([1, 2, 3], 2))
