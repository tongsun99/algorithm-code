#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = 0
        b = 0
        while True:
            a = nums[a]
            b = nums[nums[b]]
            if a == b:
                break
        a = 0
        while True:
            a = nums[a]
            b = nums[b]
            if a == b:
                break
        return a

# @lc code=end
