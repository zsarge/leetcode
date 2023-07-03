class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(lambda: [])
        for s in strs:
            groups[str(sorted(s))].append(s)
        return groups.values()