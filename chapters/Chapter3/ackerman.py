def myAckerman(m: int, n: int):
    if m == 0:
        return n + 1
    elif n > 0:
        return myAckerman(m - 1, myAckerman(m, n -1))
    elif n == 0:
        return myAckerman(m - 1, 1)

def ackermann(m: int, n: int, indentation=0):
    print(f"{' '*indentation}ackermann({m},{n})")

    if m == 0:
        #BASE CASE
        return n + 1
    elif m > 0 and n == 0:
        #RECURSIVE CASE
        return ackermann(m - 1, 1, indentation + 1)
    elif m > 0 and n > 0:
        #RECURSIVE CASE
        return ackermann(m - 1, ackermann(m, n -1, indentation + 1))

print('starting with m = 1 n = 1:')
print(ackermann(1,1))
print('starting with m = 2 n = 3:')
print(ackermann(2,3))