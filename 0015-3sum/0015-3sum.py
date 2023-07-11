class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        indicies = {k: v for v, k in enumerate(nums)}
        return list({tuple(sorted([a, b, 0-a-b]))
            for x, a in enumerate(nums)
            for y, b in enumerate(nums[:x])
            if x != y
            if 0-a-b in indicies
            if y != indicies[0-a-b] and indicies[0-a-b] != x
        })