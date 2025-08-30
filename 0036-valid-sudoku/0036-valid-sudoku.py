class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            nums = [num for num in row if num != '.']
            if len(nums) != len(set(nums)):
                return False

        for col in range(9):
            nums = [board[row][col] for row in range(9) if board[row][col] != '.']
            if len(nums) != len(set(nums)):
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                nums = []
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        if board[r][c] != '.':
                            nums.append(board[r][c])
                if len(nums) != len(set(nums)):
                    return False
        return True
