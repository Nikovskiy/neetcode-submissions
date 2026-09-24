class Solution:
    def isValid(self, s: str) -> bool:
        s = s.split()
        for i in s:
            last = s.pop()
            if i != last:
                return False
            return True
        