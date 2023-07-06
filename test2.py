def longestSubarray(nums):
        longest = 0
        length = 0

        copy = nums

        if nums.count(1) == len(nums):
            return len(nums)-1
        
        for num in range(len(nums)-1):
            if nums[num] == 0:
                copy = nums[:num] + nums[num+1:]
                for i in copy:
                    if i == 1:
                        length += 1
                        longest = max(longest, length)
                    else:
                        length = 0
                length = 0
        return longest


nums = [0,1,0]
print(longestSubarray(nums))