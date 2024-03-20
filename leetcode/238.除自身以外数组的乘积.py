#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        res = []
        n = len(nums)
        for i in range(n):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(prefix[-1] * nums[i])
        for i in range(n):
            if i == 0:
                suffix.append(nums[n - 1 - i])
            else:
                suffix.append(suffix[-1] * nums[n - 1 - i])
        for i in range(n):
            if i == 0:
                res.append(suffix[n - 2 - i])
            elif i == n - 1:
                res.append(prefix[n - 2])
            else:
                res.append(prefix[i - 1] * suffix[n - 2 - i])
        return res
# @lc code=end
