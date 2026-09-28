class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        res = 0
        def dfs(i,j):
            if i < 0 or i >= R or j < 0 or j >= C:
                return 0
            if grid[i][j] == 0 or grid[i][j] == "#": 
                return 0
            if grid[i][j] == 1:
                grid[i][j] = "#"
                return (1 + dfs(i + 1, j) + 
                dfs(i - 1, j) +  
                dfs(i, j + 1) + 
                dfs(i, j - 1))
            
                
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    res = max(res,dfs(i,j))                   
        return res
