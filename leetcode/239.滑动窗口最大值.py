#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = [0] * len(nums)
        res = []
        hh = 0; tt = -1
        for i in range(len(nums)):
            while hh <= tt and q[hh] <= i - k: hh += 1
            while hh <= tt and nums[q[tt]] <= nums[i]: tt -= 1
            tt += 1; q[tt] = i
            if i >= k - 1: res.append(nums[q[hh]])
        return res
            

# @lc code=end
