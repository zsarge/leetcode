class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            midpoint = (low + high) // 2
            if sum(ceil(pile / midpoint) for pile in piles) > h:
                low = midpoint + 1
            else:
                high = midpoint
        return low