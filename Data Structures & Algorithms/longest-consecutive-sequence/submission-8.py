class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 0
        s = set(nums)
        start = 10000
        end = 1
        if nums == []:
            return 0
        for i in nums:
            if i - 1 in s and i - 1 < start:
                start = i - 1
            if i + 1 in s and i + 1 > end:
                end = i + 1



        return end - start + 1

