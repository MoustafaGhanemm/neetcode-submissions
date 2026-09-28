class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        res = 0

        def dfs(i,j):
            if i < 0 or i >= R or j < 0 or j >= C:
                return
            if grid[i][j] == "0": 
                return
            if grid[i][j] == "1":
                grid[i][j] = "#"
                dfs(i + 1, j)  
                dfs(i - 1, j)  
                dfs(i, j + 1) 
                dfs(i, j - 1)
                
                





        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1":
                    dfs(i,j)
                    res += 1
        return res
