#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums_set = set(nums)
        for x in nums_set:
            if (x - 1) in nums_set:
                continue
            cnt = 0
            while x in nums_set:
                x += 1
                cnt += 1
            res = max(res, cnt)
        return res


# @lc code=end
