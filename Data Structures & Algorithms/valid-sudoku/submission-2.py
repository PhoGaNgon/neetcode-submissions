class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(len(board)):
            nums_x = []
            nums_y = []
            for y in range(len(board)):
                num_x = board[x][y]
                num_y = board[y][x]
                if num_x in nums_x or num_y in nums_y:
                    return False
                if num_x != '.':
                    nums_x.append(num_x)
                if num_y != '.':
                    nums_y.append(num_y)

        for sq_x in range(0, len(board), 3):
            for sq_y in range(0, len(board), 3):
                nums = []
                for x in range(0, 3):
                    for y in range(0, 3):
                        num = board[sq_x + x][sq_y + y]
                        if num != '.' and num in nums:
                            return False
                        nums.append(num)
        return True
