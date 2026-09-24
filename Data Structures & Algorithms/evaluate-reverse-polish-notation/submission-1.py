class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens = tokens[::-1]
        res = []
        b = 0
        while len(tokens) != 0:
            a = tokens.pop()
            if a.isdigit():
                res.append(a)
            else:
                if a == '+':
                    for i in res:
                        b += int(i)
                    res = []
                elif a == '-':
                    for i in res:
                        b -= int(i)
                    res = []
                elif a == '*':
                    for i in res:
                        b *= int(i)
                    res = []
                else:
                    for i in res:
                        b = b // int(i)
                    res = []
            
            print(b)
        return b
        