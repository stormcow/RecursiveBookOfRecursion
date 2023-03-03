def factorialByIteration(number):
    product = 1
    for i in range(1, number + 1):
        product = product * i
    return product


def factorialByRecursion(number):
    if number == 1:
        return 1
    return number * factorialByRecursion(number - 1)

def factorialIterativeEmulate(nthNumber):
    callStack = []
    callStack.append({'returnAddr': 'start', 'number': nthNumber})
    returnValue = None

    while len(callStack) > 0:
        number = callStack[-1]['number']
        returnAddr = callStack[-1]['returnAddr']
        if returnAddr == 'start':
            if number == 1:
                returnValue = 1
                callStack.pop()
                continue
            else:
                callStack[-1]['returnAddr'] = 'after recursive call'
                callStack.append({'returnAddr': 'start', 'number': number - 1})
                continue
        elif returnAddr == 'after recursive call':
            returnValue = number * returnValue
            callStack.pop()
            continue
    return returnValue

print(factorialByIteration(5))
print(factorialByRecursion(5))
print(factorialIterativeEmulate(5))
