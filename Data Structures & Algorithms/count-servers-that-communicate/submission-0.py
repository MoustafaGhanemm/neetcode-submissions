class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])

        hashmap_i = defaultdict(int)
        hashmap_j = defaultdict(int)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    hashmap_i[i] += 1
                    hashmap_j[j] += 1

        res_count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and (hashmap_i[i] > 1 or hashmap_j[j] > 1):
                    res_count += 1

        return res_count
                




