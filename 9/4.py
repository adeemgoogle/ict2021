def sumOfUnique(nums):
    s = {}
    for i in nums:
        if i not in s: # unique
            s[i] = 1
        else:
            s[i] += 1
    s1 = 0
    for k, v in s.items(): # пробегаемся по дикшн
        if v == 1: # if element is unique
            s1 = s1 + k # считаем сумму юник элементов
    return s1
nums = input().split()
print(sumOfUnique(nums))