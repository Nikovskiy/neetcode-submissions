
class Solution:

    def encode(self, strs: list[str]):
        i = 0
        if strs == []:
            return ''
        string = ''
        while i < len(strs):
            line = strs[i]
            if line == '':
                line = 'space'
            string += line
            string += '|||||'
            i += 1
        return string.strip('|||||')
    def decode(self, s: str):
        if s == '':
            return []
        strs = s.split('|||||')
        i = 0
        while i < len(strs):
            if strs[i] == 'space':
                strs[i] = ''
            i += 1
        return strs