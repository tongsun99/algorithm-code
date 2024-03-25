#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # 看在哪一行
        i = 0
        while i <= m - 1:
            if matrix[i][0] > target:
                break
            i += 1
        # i - 1行
        i -= 1
        l = 0
        r = n - 1
        while l < r:
            mid = (l + r) // 2
            if matrix[i][mid] < target:
                l = mid + 1
            else:
                r = mid

        return matrix[i][l] == target
# @lc code=end

