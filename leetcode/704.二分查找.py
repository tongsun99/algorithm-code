#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0; r = len(nums) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] > target: r = mid - 1
            else: l = mid
        if nums[l] != target: return -1
        return l
# @lc code=end

