#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
from collections import deque


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        i = n - 1
        # f[i]表示从i跳到终点的最短步数
        f = [float("inf")] * n
        f[-1] = 0
        while i >= 0:
            for j in range(1, nums[i] + 1):
                x = i + j
                if x >= n - 1:
                    x = n - 1
                f[i] = min(f[i], f[x] + 1)
            i -= 1
        return int(f[0])
             
# @lc code=end
