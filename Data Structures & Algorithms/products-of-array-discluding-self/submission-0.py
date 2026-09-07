class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        suff= []
        i = 0
        pr1 = 1
        pr2 = 1
        output = []
        while i < len(nums):

            pref.append(nums[i] * pr1)
            pr1 = nums[i] * pr1

            suff.append(nums[len(nums) - 1 - i] * pr2)
            pr2 = nums[len(nums) - 1 - i] * pr2
            i += 1
        j = 0
        while j < len(nums):
            if j == 0 :
                output.append(suff[len(nums) - 2])
            elif j == len(nums) - 1:
                print(pref[len(nums) - 1])
                output.append(pref[len(nums) - 2])
            else:
                output.append(pref[j - 1] * suff[len(nums) - 2 - j])
            j += 1

        return output
