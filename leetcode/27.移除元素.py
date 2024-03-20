#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1:
            if nums[0] == val: return 0
            else: return 1
        i = 0
        j = len(nums) - 1
        while i < j:
            while i < len(nums) and nums[i] != val: i += 1
            while j >= 0 and nums[j] == val: j -= 1
            if i < j: nums[i], nums[j] = nums[j], nums[i]
        return i
# @lc code=end

