from typing import List
def concat(array: List[str]):
    if len(array) == 0:
        return ''
    return array[0] + concat(array[1:])

words = ['ala','ma','kota']
words2 = ['hello','world']
print(concat(words))
print(concat(words2))