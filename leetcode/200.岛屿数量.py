#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        m = len(grid)
        n = len(grid[0])
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        # vis = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                # bfs
                if grid[i][j] == '0': continue
                q = deque([])
                q.append((i, j))
                # grid[i][j] = '0'
                res += 1
                while q:
                    x, y = q[0]
                    grid[x][y] = '0'
                    q.popleft()
                    for k in range(4):
                        x_ = x + dx[k]
                        y_ = y + dy[k]
                        if x_ >= 0 and x_ <= (m - 1) and y_ >= 0 and y_ <= (n - 1) and grid[x_][y_] == '1':
                            q.append((x_, y_))
                            grid[x_][y_] = '0'
                        
        return res


                
        
# @lc code=end

