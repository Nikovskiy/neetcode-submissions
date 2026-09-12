class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        j = 0
        result = []
        while i < len(nums) - 2:
            j  = i + 1
            target = -nums[i]
            k = len(nums) - 1
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            if nums[i] > 0:
                break
            while j < k:
                if nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
                
            i += 1
            
                
        
        return result  