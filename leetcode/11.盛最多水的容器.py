# @before-stub-for-debug-begin
from python3problem11 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        res = 0
        while i < j:
            print(f'{height[i]} {height[j]}')
            cur_height = min(height[i], height[j])
            cur_area = cur_height * (j - i)
            res = max(res, cur_area)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return res

# @lc code=end
