class Solution:
    def isValid(self, s: str) -> bool:
        s = [i for i in s]
        stack = []
        dct = {")":"(","]":"[","}":"{"}
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if stack[-1] != dct[i]:
                    return False
                else:
                    stack.pop()
        return True

        