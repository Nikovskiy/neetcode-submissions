class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        mx = 0
 
        for i in nums:

            if i - 1 not in s:

                start = i
                length = 1
                while start + 1 in s:
                    start += 1
                    length += 1
                if length > mx:
                    mx = length
        return mx

