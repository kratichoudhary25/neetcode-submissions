class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        groups = []
        for i in range(len(strs)):
            j = strs[i]
            j = ''.join(sorted(j))
            if j in ana.keys():
                ana[j].append(strs[i])
            else:
                ana[j] = [strs[i]]

        return list(ana.values())