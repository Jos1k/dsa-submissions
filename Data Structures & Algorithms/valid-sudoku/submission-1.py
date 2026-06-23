class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
    
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue

                num = int(board[i][j])
                square = (i // 3) * 3 + (j // 3)
                if num in rows[i] or num in cols[j] or num in squares[square]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                squares[square].add(num)

        return True
            