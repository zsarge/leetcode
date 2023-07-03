class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(lambda: 0)
        for num in nums:
            counter[num] += 1
        return sorted(set(nums), key=lambda num: counter[num], reverse=True)[:k]