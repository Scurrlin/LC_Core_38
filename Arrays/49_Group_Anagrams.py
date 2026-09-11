from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            sortedWord = tuple(sorted(word))
            group[sortedWord].append(word)
        return list(group.values())