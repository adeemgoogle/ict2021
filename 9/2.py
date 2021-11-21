def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted(nums) # надо обязательно отсортить лист для удобства
    dict_pos = {}
    number_of_smaller = 0
    for e in sorted_nums:
        if e not in dict_pos:
            dict_pos[e] = number_of_smaller
        number_of_smaller += 1 # если есть дубликаты ++
    res = []
    for e in nums: #
        res.append(dict_pos[e])
    return res

nums = input().split()
print(smallerNumbersThanCurrent(nums))