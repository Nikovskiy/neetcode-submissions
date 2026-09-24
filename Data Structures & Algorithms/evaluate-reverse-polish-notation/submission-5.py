class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.isdigit():
                stack.append(int(i))
            else:
                if len(stack) == 1:
                    return stack[-1]
                elif i == '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                elif i == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a + b)
                elif i == '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a * b)
                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b // a)
        return stack[-1]