class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copy = sorted(nums)
        start = 0
        end = len(nums)-1
        while start < end:
            result = copy[start] + copy[end]
            if result == target:
                lastIndex = len(nums) -nums[::-1].index(copy[end])-1
                return [nums.index(copy[start]), lastIndex]
            elif result < target:
                start += 1
            elif result > target:
                end -= 1
        raise Exception(f"Invalid Input {nums}")