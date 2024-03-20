#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        vis = []
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        def dfs(x, y, cur):
            # print(f'x: {x}, y: {y}, cur: {cur}')
            if cur == word:
                return True
            for dir in range(4):
                x_ = x + dx[dir]
                y_ = y + dy[dir]
                if x_ >= 0 and x_<= m - 1 and y_ >=0 and y_ <= n - 1 and vis[x_][y_] == 0 \
                    and word.startswith(cur + board[x_][y_]):
                    vis[x_][y_] = 1
                    if dfs(x_, y_, cur+board[x_][y_]): return True
                    vis[x_][y_] = 0
        
        for i in range(m):
            for j in range(n):
                vis = [[0] * n for _ in range(m)]
                if board[i][j] == word[0]:
                    vis[i][j] = 1
                    if dfs(i, j, board[i][j]): return True
        return False
# @lc code=end

