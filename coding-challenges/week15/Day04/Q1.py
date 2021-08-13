class Solution(object):
    def minMoves(self, nums):
        if not nums:
            return 0
        res = 0
        nums.sort()
        for i in range(1, len(nums)):
            res += nums[i] - nums[0]
        return res