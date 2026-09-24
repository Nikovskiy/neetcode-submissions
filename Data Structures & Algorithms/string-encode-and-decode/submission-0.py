class Solution:

    def encode(self, strs: List[str]) -> str:
        i = 0
        string = ''
        while i < len(strs):
            string += strs[i]
            string += ' '
            i += 1
        return string.strip()
    def decode(self, s: str) -> List[str]:
        strs = s.split()
        i = 0
        while i < len(strs):
            strs[i] = strs[i]
            i += 1
        if strs == []:
            strs = ['']
        return strs
