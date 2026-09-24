class Solution:
    def isValid(self, s: str) -> bool:
        s = [i for i in s]
        stack = []
        dct = {")":"(","]":"[","}":"{"}
        if len(s) < 2:
            return False
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if stack:
                    if stack.pop() != dct[i]:
                        return False
                else:
                    return False

                    
        return True

        