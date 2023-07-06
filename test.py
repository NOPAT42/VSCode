def intersection(nums):
    duplicate = []
    num = []
    
    for i in range(len(nums)):
        num += nums[i]

    for i in num:
        if num.count(i) == len(nums) and i not in duplicate:
            duplicate.append(i)

    duplicate.sort()
    return duplicate


nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
print(intersection(nums))
