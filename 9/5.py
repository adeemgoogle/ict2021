def uuniq(nums):
    dic = {}
    for i in nums: # i пробегаемся по листу
        if i in dic: # если он есть в дикшн то делаем ++
            dic[i] += 1
        else:
            dic[i] = 1
    if len(set(dic.values())) != len(set(nums)): # если изначальный лист сайз != дикшн сайз значит не юник
        return False
    return True
nums = input().split()
print(uuniq(nums))