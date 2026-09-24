class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        result = []
        for word in strs:
            key = ''.join(sorted(set(word)))
            if key in dct:
                dct[key].append(word)
            else:
                dct[key] = [word]
        for i in dct:
            result.append(dct[i])
        return result



            




        