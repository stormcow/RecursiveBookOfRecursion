def rev(theString: str, accum: str = "") -> str:
    if len(theString) == 0:
        return accum
    else:
        head: str = theString[0]
        tail: str = theString[1:]
        return rev(tail, head + accum)


text = "abcdef"
print(rev(text))
