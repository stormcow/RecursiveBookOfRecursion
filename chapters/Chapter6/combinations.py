def getCombos(chars: str, k: int) -> list[str]:
    if k == 0:
        return [""]
    elif chars == "":
        return []

    combinations = []
    head = chars[:1]
    tail = chars[1:]
    tailCombos = getCombos(tail, k - 1)
    for tailCombo in tailCombos:
        combinations.append(head + tailCombo)

    combinations.extend(getCombos(tail, k))

    return combinations


print(getCombos("abc", 2))
