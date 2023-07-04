class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        result = []
        for a in set(nums1):
            for _ in range(min(count1[a], count2[a])):
                result.append(a)
        return result