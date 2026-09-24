class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dct = {}
        for word in strs:
            if frozenset(word) not in dct:
                dct[frozenset(word)] = [word]
            else:
                dct[frozenset(word)].append(word)
        for i in dct:
            result.append(dct[i])
        return result



            




        