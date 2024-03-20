#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_0 = 0
        num_1 = 0
        num_2 = 0
        for num in nums:
            if num == 0:
                num_0 += 1
            if num == 1:
                num_1 += 1
            if num == 2:
                num_2 += 1
        nums[0:num_0] = [0] * num_0
        nums[num_0:num_0+num_1] = [1] * num_1
        nums[num_0+num_1:] = [2] * num_2
# @lc code=end
