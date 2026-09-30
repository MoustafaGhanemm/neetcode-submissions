class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r,c = len(board), len(board[0])

        def dfs(i,j):
            if i >= r or i < 0 or j>= c or j < 0 or board[i][j] != "O":
                return
            board[i][j] = "T"
            dfs(i + 1,j)
            dfs(i - 1,j)
            dfs(i,j + 1)
            dfs(i,j - 1)


        

        for i in range(r):
            for j in range(c):
                if board[i][j] == "O" and (i == 0 or i == r - 1 or j == 0 or j == c - 1):
                    dfs(i,j)
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"


