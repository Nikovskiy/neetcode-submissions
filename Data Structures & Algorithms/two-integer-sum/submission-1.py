class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        dct = {}
        while i < len(nums):
            n = target - nums[i]
            if n not in dct:
                dct[nums[i]] = i
                i += 1
            else:
                a = dct[n]
                b = i
                return [ a, b]
            
         
            

        