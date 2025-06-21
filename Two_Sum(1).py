class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

# Test it
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
