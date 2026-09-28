class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        used = set()
        def dfs(subset):
            if len(subset) == len(nums):
                output.append(subset.copy())
                return
            
            for num in nums:
                if num in used:
                    continue
                else:
                    subset.append(num)
                    used.add(num)
                    dfs(subset)
                    subset.pop()
                    used.remove(num)
        dfs([])
        return output


