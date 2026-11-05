class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for str in strs:
            sortedStr = ''.join(sorted(str))
            if sortedStr in groups:
                groups[sortedStr].append(str)
            else:
                groups[sortedStr] = [str]

        res = []
        for key in groups:
            res.append(groups[key])

        return res