class Solution:
    def isValid(self, s: str) -> bool:
        s = [i for i in s]
        dct = {")":"(","]":"[","}":"{"}
        for i in s:
            print(i)
            last = s.pop()
            print(last)
            if i != dct[last]:
                return False
            return True
        