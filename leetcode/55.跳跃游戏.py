#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        rightmost = nums[0]
        for i in range(len(nums)):
            if i > rightmost: return False
            rightmost = max(rightmost, i + nums[i])
            if rightmost >= len(nums) - 1: return True
        return True
        
# @lc code=end

