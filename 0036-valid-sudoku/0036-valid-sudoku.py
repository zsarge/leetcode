class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def contains_duplicates(arr):
            nums = [int(n) for n in arr if n in string.digits]
            return len(set(nums)) != len(nums)
        for row in board:
            if contains_duplicates(row):
                return False
        rot90 = [[board[y][x] for y in range(len(board))]
               for x in reversed(range(len(board[0])))]
        for row in rot90:
            if contains_duplicates(row):
                return False
        for dx in range(0, 9, 3):
            for dy in range(0, 9, 3):
                chunk = [line[dx:dx+3] for line in board[dy:dy+3]]
                if contains_duplicates(reduce(concat, chunk)):
                    return False
        return True
