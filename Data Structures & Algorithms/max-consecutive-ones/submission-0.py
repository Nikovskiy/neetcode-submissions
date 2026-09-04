class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        counter = 0
        for i in nums:
            
            if i != 0:
                counter+=i
            else:
                counter = 0
            if counter> max:
                 max = counter
        return max
        