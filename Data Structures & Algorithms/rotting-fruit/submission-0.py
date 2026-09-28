class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        res = 0
        good = 0
        direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    good += 1
        


        while q and good:
            for i in range(len(q)):
                idx1, idx2 = q.popleft()
                for x,y in direct:
                    ni, nj = idx1 + x, idx2 + y
                    if ni < 0 or ni >= R or nj < 0 or nj >= C:
                        continue
                    elif grid[ni][nj] == 1:
                        q.append((ni,nj))
                        grid[ni][nj] = 2
                        good -= 1
            res += 1
        
        return res if good == 0 else -1

                    


                
        