class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        R, C = len(board), len(board[0])
        def dfs(i, j, k):
            if len(word) == k:
                return True
            if i < 0 or i >= R or j < 0 or j >= C:
                return False
            if board[i][j] == word[k]:
                temp = board[i][j]
                board[i][j] = "#"
                res = (dfs(i + 1, j, k + 1) or 
                dfs(i - 1, j, k + 1) or 
                dfs(i, j + 1, k + 1) or
                dfs(i, j - 1, k + 1))
                board[i][j] = temp
                return res
            else:
                return False
        


        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False
                    
        