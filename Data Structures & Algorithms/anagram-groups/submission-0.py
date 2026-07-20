class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrMap = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key in sortedStrMap:
                sortedStrMap[key].append(str)
            else:
                sortedStrMap[key] = [str]   
        return list(sortedStrMap.values())