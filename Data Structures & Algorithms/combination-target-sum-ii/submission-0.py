class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        comb = []
        candidates.sort()
        def dfs(i, total):
            if total == target:
                output.append(comb.copy())
                return
            if len(candidates) <= i:
                return
            elif total > target:
                return
            
            comb.append(candidates[i])
            dfs(i+1, total + candidates[i])
            comb.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)
        dfs(0,0)
        return output


            
