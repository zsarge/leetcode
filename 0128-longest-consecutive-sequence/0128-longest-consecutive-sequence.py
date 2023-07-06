class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # this feels unnecessarily convoluted
        if len(nums) == 0:
            return 0
        num_set = set(nums)
        lookup = dict()
        for num in nums:
            if num + 1 in num_set:
                lookup[num] = num+1
        max_length, length = 1, 1
        for key in sorted(list(set(lookup.keys()))):
            while lookup.get(key) in lookup:
                tmp = lookup[key]
                del lookup[key]
                key = tmp
                length += 1
            else:
                length += 1
            max_length = max(max_length, length)
            length = 1
        return max_length