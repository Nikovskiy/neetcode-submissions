class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 0
        # save = set()
        s = set(nums)

        for idx, i in enumerate(nums):
            if i - 1 in s :
                counter += 1
            # save.add(i )
        if counter == 0 and len(nums) != 0:
            counter += 1
        return counter

