class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                if num in rows[i]:
                    return False

                if num in cols[j]:
                    return False

                if num in squares[i // 3, j // 3]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                squares[i // 3, j // 3].add(num)
        
        return True
                
