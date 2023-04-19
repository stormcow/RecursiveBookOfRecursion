def getPowerSet(chars: str) -> list[str]:
    if chars == "":
        return [""]

    powerSet = []
    head = chars[0]
    tail = chars[1:]

    tailPowerSet = getPowerSet(tail)

    for tailSet in tailPowerSet:
        powerSet.append(head + tailSet)

    powerSet = powerSet + tailPowerSet

    return powerSet


mySet = getPowerSet("abc")
mySet.sort(key=len)
print(mySet)
