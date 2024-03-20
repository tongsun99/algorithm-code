#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        i = 0
        prev = 100005
        for i in range(len(nums)):
            if nums[i] == prev:
                continue
            prev = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    tmp = nums[l]
                    while l <= len(nums) - 1 and nums[l] == tmp: l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    # r右移
                    tmp = nums[r]
                    while r >= 0 and nums[r] == tmp: r -= 1
                else:
                    # l左移
                    tmp = nums[l]
                    while l <= len(nums) - 1 and nums[l] == tmp: l += 1
        return res
            
# @lc code=end
