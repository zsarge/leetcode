class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        # '<=' because we have to check the midpoint
        while low <= high:
            midpoint = (low + high)//2 # '//' represents integer division
            if nums[midpoint] == target:
                return midpoint
            elif target < nums[midpoint]:
                high = midpoint - 1
            else: # target > nums[midpoint]
                low = midpoint + 1
        
        return -1
        