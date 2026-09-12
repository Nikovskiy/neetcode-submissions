class Solution:
    def isValid(self, s: str) -> bool:
      
        stack = []
        dct = {")":"(","]":"[","}":"{"}

        if len(s) < 1:
            return False
            
        for i in s:
            if i in '({[':

                stack.append(i)
            elif stack:
                last = stack.pop()
                if last != dct[i]:
                    return False
            else:
                return False

        if stack == []:
            return True
        else:
            return False

        