class Solution:
    def findRow(self, matrix: List[List[int]], target: int) -> List[int]:
        # find the row
        low = 0
        high = len(matrix)-1
        while low <= high:
            midpoint = (low + high)//2
            if matrix[midpoint][0] <= target <= matrix[midpoint][-1]:
                return matrix[midpoint]
            elif target < matrix[midpoint][0]:
                high = midpoint - 1
            else: # target > matrix[midpoint][-1]:
                low = midpoint + 1
        return None
    def findColumn(self, row: List[int], target: int) -> bool:
        low, high = 0, len(row) - 1
        while low <= high:
            midpoint = (low + high)//2
            if row[midpoint] == target:
                return True
            elif target < row[midpoint]:
                high = midpoint - 1
            else: # target > row[midpoint]
                low = midpoint + 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        row = self.findRow(matrix, target)
        if row is None:
            return False
        return self.findColumn(row, target)