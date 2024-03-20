#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = 0
        j = 0

        for i in range(n//2):
            for j in range(i + 1, n - i):
                pos1 = matrix[i][j]
                pos2 = matrix[j][n-i-1]
                pos3 = matrix[n-i-1][n-j-1]
                pos4 = matrix[n-j-1][i]
                matrix[i][j] = pos4
                matrix[j][n-i-1] = pos1
                matrix[n-i-1][n-j-1] = pos2
                matrix[n-j-1][i] = pos3

# @lc code=end
