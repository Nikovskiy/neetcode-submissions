class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 0
        save = set()
        s = set(nums)
        if len(nums) == 1:
            return 1
        for i in nums:
            if i + 1 in s and i + 1 not in save:
                counter += 1
        return counter

