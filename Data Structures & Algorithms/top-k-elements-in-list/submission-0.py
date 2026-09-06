class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for i in nums:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        lst = list(sorted(dct.items(), key=lambda x: x[1], reverse=True))
        tops = [i[0] for i in lst[:k]]
        return tops

        