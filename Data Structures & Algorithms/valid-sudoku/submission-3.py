class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        sqrs = [0] * 9

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                sqr = (i // 3) + ((j // 3) * 3)
                mask = 1 << (int(val) - 1)
                if rows[i] & mask:
                    return False
                elif cols[j] & mask:
                    return False
                elif sqrs[sqr] & mask:
                    return False
                rows[i] |= mask
                cols[j] |= mask
                sqrs[sqr] |= mask
        return True
