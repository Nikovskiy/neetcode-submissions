class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dct = {}
        for word in strs:
            sm = 0
            for i in word:
                sm += ord(i)
            if sm in dct:
                dct[sm].append(word)
            else:
                dct[sm] = [word]
                

        for i in dct:
            result.append(dct[i])
        return result



            




        