#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#

# @lc code=start
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # print(m, n)
        q = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        d = 0
        while q:
            x, y, d = q[0]
            q.popleft()
            for i in range(4):
                x_ = x + dx[i]
                y_ = y + dy[i]
                if x_ >= 0 and x_ <= (m - 1) and y_ >= 0 and y_ <= (n - 1) and grid[x_][y_] == 1:
                    q.append((x_, y_, d + 1))
                    grid[x_][y_] = 2
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: return -1
        
        return d

        
        
        
# @lc code=end

