class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dct = {}
        dct2 = {}
        st = ''
        for word in strs:
            sm = 0

            for i in word:
                sm += ord(i)
                st = frozenset(word)

            if st in dct and dct2[st] == sm:
                dct[st].append(word)
            else:
                dct[st] = [word]
                dct2[st] = sm
                

        for i in dct:
            result.append(dct[i])
        return result



            




        