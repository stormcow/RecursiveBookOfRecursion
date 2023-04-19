def getPermsWithRep(chars: str, permLength: int = None, prefix: str = "") -> list[str]:
    if permLength is None:
        permLength = len(chars)

    if permLength == 0:
        return [prefix]

    results = []
    for char in chars:
        newPrefix = prefix + char
        results.extend(getPermsWithRep(chars, permLength - 1, newPrefix))
    return results


print(getPermsWithRep("JPB123", 8))
