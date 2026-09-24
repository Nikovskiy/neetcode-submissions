class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        j = len(nums) - 1
        result = []
        while i != j + 2:
            k = i + 1
     
            while k < j:
    
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
                k += 1


            if i - j % 2 == 0:
                i += 1
            else:
                j -= 1
        return result  
