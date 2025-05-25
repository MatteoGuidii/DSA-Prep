class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows =    [set() for _ in range(9)] # rows[i]  tracks all seen digits in row i (0–8)
        columns = [set() for _ in range(9)] # cols[j]  tracks all seen digits in column j (0–8)
        boxes =   [set() for _ in range(9)] # boxes[k] tracks all seen digits in 3×3 block k (0–8)

        
        for r in range(n):
            for c in range(n):
                value = board[r][c]
                if value != '.':

                    # Compute which 3×3 box we're in:
                    # (r//3) is 0 for rows 0–2, 1 for rows 3–5, 2 for rows 6–8
                    # (c//3) is 0 for cols 0–2, 1 for cols 3–5, 2 for cols 6–8
                    # multiply the row-block by 3 to jump to box indices 0,3,6
                    # then add the col-block (0,1,2) to land in the correct box (0–8)
                    b = (r // 3) * 3 + (c // 3)

                    if value in rows[r] or value in columns[c] or value in boxes[b]:
                        return False

                    rows[r].add(value)
                    columns[c].add(value)
                    boxes[b].add(value)

        return True

# Time Complexity:
#   – O(1) for the fixed 9×9 board: we do 9×9 = 81 iterations, each doing O(1) work → O(81) = O(1).
#   – If generalized to an N×N board, it would be O(N²): two nested loops over N rows and N cols, each with O(1) set ops.
#
# Space Complexity:
#   – O(1) for the fixed 9×9 board: at most 9 sets × 3 × 9 entries = 243 entries total → constant.
#   – If generalized to an N×N board, it would be O(N²): 3 groups (rows, cols, boxes) of N sets, each holding up to N items → O(3N²) = O(N²).
