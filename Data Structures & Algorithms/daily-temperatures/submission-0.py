class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        result = [0] * len(temperatures)
        for idx, i in enumerate(temperatures):
            while res and temperatures[res[-1]] < i:
                j = res.pop()
                result[j] = idx - j
            res.append(idx)
        return result
