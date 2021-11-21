def numpairs(nums):
    pairs = {}
    num = 0
    for v in nums: # i пробегаемся по листу
        if v in pairs: # чекаем есть ли он в дикшн
            pairs[v] += 1
        else:
            pairs[v] = 1
    for i in pairs: # i пробегаемся дикшн
        value = pairs[i]
        for j in range(value): # еще раз чекаем есть ли еще такой же элемент
            num+=j
    return num
nums = input().split()
print(numpairs(nums))
