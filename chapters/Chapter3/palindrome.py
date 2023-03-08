def myPalindrome(string: str):
    if len(string) == 0 or len(string) == 1:
        return True
    else:
        head = string[0]
        last = string[-1] 
        middle = string[1:-1]
        return head == last and myPalindrome(middle)

text = 'racecar'
print(myPalindrome(text))