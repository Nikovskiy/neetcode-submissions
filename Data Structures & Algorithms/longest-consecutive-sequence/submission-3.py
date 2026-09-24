class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 0
        # save = set()
        s = set(nums)
        # if len(nums) == 1:
        #     return 1
        for idx, i in enumerate(nums):
            if i + 1 in s or idx == 0:
                counter += 1
            # save.add(i )
            
        return counter

