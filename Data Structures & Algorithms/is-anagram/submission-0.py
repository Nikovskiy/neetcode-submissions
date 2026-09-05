class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct_s = {}
        dct_t = {}
        for i in s:
            if i in dct_s:
                dct_s[i] += 1
            else:
                dct_s[i] = 1
        for i in t:
            if i in dct_t:
                dct_t[i] += 1
            else:
                dct_t[i] = 1
        if dct_t == dct_s:
            return True
        else:
            return False