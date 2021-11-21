def repeatedNTimes(nums):
    dic = {}
    for i in nums:
        if i in dic: # cheaking in dict if yes ++
            dic[i] += 1
            if dic[i] == len(nums) / 2:
                return i # Return the element that is repeated n times
        else:
            dic[i] = 1
nums = input().split()
print(repeatedNTimes(nums))