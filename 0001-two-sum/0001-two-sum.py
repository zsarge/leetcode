class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x, a in enumerate(nums):
            for y, b in enumerate(nums):
                if x != y and a + b == target:
                    return [x, y]
        raise Exception(f"Invalid Input {nums}")