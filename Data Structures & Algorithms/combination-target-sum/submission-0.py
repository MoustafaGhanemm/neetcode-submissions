class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        comb = []
        def dfs(i, total):
            if len(nums) <= i:
                return
            
            if total == target:
                output.append(comb.copy())
                return
            elif total > target:
                return
            comb.append(nums[i])
            dfs(i , total + nums[i])
            comb.pop()
            dfs(i + 1, total)
        dfs(0,0)
        return output
            
            