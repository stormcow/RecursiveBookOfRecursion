def shortestWithBaseCase(makeRecursiveCall):
    print('shorestWithBaseCase (%s) called.'% makeRecursiveCall)
    if not makeRecursiveCall:
        #BASE CASE
        print('Returning from base case')
        return
    else:
        #RECURSIVE CASE
        shortestWithBaseCase(False)
        print('Returning from recursive case')
        return
    
print('Calling shortestWithBaseCase(False:')
shortestWithBaseCase(False)
      
print('\nCalling shorestWithBaseCase(True):')
shortestWithBaseCase(True)