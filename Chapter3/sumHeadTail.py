def sum(numbers):
    if len(numbers) == 0:
        return 0
    else:
        head = numbers[0]
        tail = numbers[1:]
        return head + sum(tail)


nums = [1, 2, 3, 4, 5]
print(f'The sum of {nums} is {sum(nums)}')
nums = [5, 2, 4, 8]
print(f'The sum of {nums} is {sum(nums)}')
nums = [1, 10, 100, 1000]
print(f'The sum of {nums} is {sum(nums)}')
