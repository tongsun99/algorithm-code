#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = nums.copy()
        dp_min = nums.copy()
        for i in range(1, n):
            dp_max[i] = max(nums[i], dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i])
            dp_min[i] = min(nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])

        return max(dp_max)
# @lc code=end

