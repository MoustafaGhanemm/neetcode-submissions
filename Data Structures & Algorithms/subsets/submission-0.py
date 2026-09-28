class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dfs(curr, i):
            if i == len(nums):
                output.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(curr,i+1)
            curr.pop()
            dfs(curr, i + 1)
        
        dfs([],0)

        return output
