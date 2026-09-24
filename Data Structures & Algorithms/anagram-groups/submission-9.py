class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dct = {}
        dct2 = {}

        for word in strs:
            sm = 0
            st = frozenset(word)
            for i in word:
                sm += ord(i)
            dct2[sm] = st   

            if st in dct and dct2[sm] == st:
                dct[st].append(word)
            else:
                dct[st] = [word]
                dct2[sm] = st
                

        for i in dct:
            result.append(dct[i])
        return result



            




        