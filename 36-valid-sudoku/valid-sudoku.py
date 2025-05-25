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
                    b = (r // 3) * 3 + (c // 3)

                    if value in rows[r] or value in columns[c] or value in boxes[b]:
                        return False

                    rows[r].add(value)
                    columns[c].add(value)
                    boxes[b].add(value)

        return True