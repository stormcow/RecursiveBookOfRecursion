def myReverse(string: str):
    if len(string) == 0:
        return ''
    elif len(string) == 1:
        return string
    else:
        head = string[0]
        tail = string[1:]
        return myReverse(tail) + head

print(myReverse("CAT IS LONG"))