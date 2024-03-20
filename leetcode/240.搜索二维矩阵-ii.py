#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        vis = [[0] * n for _ in range(m)]
        global res
        res = False
        

        def dfs(i, j, vis, tgt):
            # print(f'i:{i}, j:{j}')
            vis[i][j] = 1
            if matrix[i][j] == tgt:
                return True
            if matrix[i][j] < tgt:
                if i + 1 >= 0 and i + 1 <= m - 1 and j >= 0 and j <= n - 1 and vis[i+1][j] == 0:
                    vis[i+1][j] = 1
                    if dfs(i+1, j, vis, tgt): return True
                if i >= 0 and i <= m - 1 and j + 1 >= 0 and j + 1 <= n - 1 and vis[i][j+1] == 0:
                    vis[i][j + 1] = 1
                    if dfs(i, j + 1, vis, tgt): return True
            if matrix[i][j] > tgt:
                if i - 1 >= 0 and i - 1 <= m - 1 and j >= 0 and j <= n - 1 and vis[i-1][j] == 0:
                    vis[i-1][j] = 1
                    if dfs(i-1, j, vis, tgt): return True
                if i >= 0 and i <= m - 1 and j - 1 >= 0 and j - 1 <= n - 1 and vis[i][j-1] == 0:
                    vis[i][j-1] = 1
                    if dfs(i, j - 1, vis, tgt): return True
            return False

        return dfs(0, 0, vis, target)
# @lc code=end
