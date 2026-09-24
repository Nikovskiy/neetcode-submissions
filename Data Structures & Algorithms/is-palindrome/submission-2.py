class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i.lower() for i in s if i.isalpha()])
        start = 0
        end = len(s) - 1
        if s == '':
            return True
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True