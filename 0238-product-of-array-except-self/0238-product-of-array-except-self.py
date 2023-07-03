class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        
        acc = 1
        for i, num in enumerate(nums):
            result[i] = acc
            acc *= num
        
        acc = 1
        for i, num in reversed(list(enumerate(nums))):
            result[i] *= acc
            acc *= num
        
        # acc = 1
        # for i, num in enumerate(nums):
        #     result[i] = acc
        #     acc *= num

        # result[0] =     2 * 3 * 4
        # result[1] = 1 *     3 * 4
        # result[2] = 1 * 2     * 4
        # result[3] = 1 * 2 * 3

        # result[0] = 
        # result[1] = result[0] 
        # result[2] = result[0] * result[1]
        # result[3] = result[1] * result[2]

        # result[3] = result[3]
        # result[2] = result[0] 
        # result[1] = result[0] * result[1]
        # result[0] = result[1] * result[2]

        return result