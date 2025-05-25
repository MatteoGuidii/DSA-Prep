class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows =    [set() for _ in range(9)] # rows[i]  tracks all seen digits in row i (0–8)
        columns = [set() for _ in range(9)] # cols[j]  tracks all seen digits in column j (0–8)
        boxes =   [set() for _ in range(9)] # boxes[k] tracks all seen digits in 3×3 block k (0–8)

        r = c = 0
        for _ in range(81):
            curr_elem = board[r][c]
            if curr_elem != '.':
                b = (r // 3) * 3 + (c // 3)
                if curr_elem in rows[r] or curr_elem in columns[c] or curr_elem in boxes[b]:
                    return False
                rows[r].add(curr_elem)
                columns[c].add(curr_elem)
                boxes[b].add(curr_elem)
            
            # Go to the next cell
            c += 1
            if c == 9:
                c = 0
                r += 1
            
        return True