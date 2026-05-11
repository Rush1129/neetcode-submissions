class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sdict = dict()

        for s in strs:
            sorted_strs = ''.join(sorted(s))

            if sorted_strs not in sdict:
                sdict[sorted_strs] = []
            sdict[sorted_strs].append(s)

        return list(sdict.values())

            