class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(len(board)):
            nums = []
            for y in range(len(board)):
                num = board[x][y]
                if num != '.' and num in nums:
                    return False
                nums.append(num)

        for x in range(len(board)):
            nums = []
            for y in range(len(board)):
                num = board[y][x]
                if num != '.' and num in nums:
                    return False
                nums.append(num)

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
