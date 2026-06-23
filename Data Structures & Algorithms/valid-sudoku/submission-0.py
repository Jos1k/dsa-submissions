class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
    
        for i in range(len(board)):
            row = [False] * (n+1)
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue

                num = int(board[i][j])

                if row[num] == True:
                    return False
                row[num] = True
        
        for i in range(len(board[0])):
            column = [0] * (n+1)
            for j in range(len(board)):
                if board[j][i] == '.':
                    continue

                num = int(board[j][i])
                if column[num] == True:
                    return False

                column[num] = True
        
            squares=[List[str]]*n
            for i in range(n):
                squares[i] = [False] * (n+1)

            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == '.':
                        continue
                    square = (i // 3) * 3 + (j // 3)
                    num = int(board[i][j])
                    
                    if squares[square][num] == True:
                        return False
                    squares[square][num] = True

        return True
            