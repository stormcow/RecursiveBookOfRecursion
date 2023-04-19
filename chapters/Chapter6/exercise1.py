def getPerms(array: list) -> list:
    if len(array) == 1:
        return [array]

    permutations = []
    head = [array[0]]
    tail = array[1:]
    tailPermutations = getPerms(tail)
    for tailPerm in tailPermutations:
        for i in range(len(tailPerm) + 1):
            newPerm = tailPerm[0:1] + head + tailPerm[i:]
            permutations.append(newPerm)
    return permutations


print(getPerms(["a", "b", "c"]))
