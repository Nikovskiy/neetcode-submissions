class Solution:
    def isValid(self, s: str) -> bool:
        s = [i for i in s]
        dct = {")":"(","]":"[","}":"{"}
        for i in s:

            last = s.pop()

            if i == dct[last]:
                return True
            return False
        