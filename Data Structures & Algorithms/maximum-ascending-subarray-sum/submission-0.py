class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        mc = nums[0]
        i = 0

        length = len(nums)
        for i in range(len(nums)):
            count = nums[i]
            while i < length and i + 1 < length and nums[i] < nums[i+1]:
                print(nums[i+1])
                count += nums[i+1]
                i = i + 1
            mc = max(mc,count)
        return mc
            