#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = nums[i]
        
        for i in range(len(nums)):
            if i >= 1:
                dp[i] = max(dp[i], dp[i - 1])
            if i >= 2:
                dp[i] = max(dp[i], dp[i - 2] + nums[i])
        return dp[-1]
# @lc code=end

