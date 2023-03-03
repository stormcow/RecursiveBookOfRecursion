def iterative(number: int):
    i = 0
    while i < number:
        print(i, 'hello')
        i += 1

def recursive(number: int, i = 0):
    print(i, 'hello')
    i+=1
    if i < number:
        recursive(number, i)
    else:
        return

recursive(5)
#iterative(5)