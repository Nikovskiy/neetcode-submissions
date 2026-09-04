class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        i = 0
        while i < len(nums):
            if nums[i] == val:
                k -= 1
                nums.pop(i)
                nums.append('_')
                i -= 1
            i += 1
        return k
            
        