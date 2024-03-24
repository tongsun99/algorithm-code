#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        f = [[0] * (m + 5) for _ in range(n + 5)]
        word1 = " " + word1
        word2 = " " + word2
        # f[i][j]: 将word1的前i个字符变为word2的前j个字符的最少步数
        # init
        for i in range(1, n + 1): f[i][0] = i
        for i in range(1, m + 1): f[0][i] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                f[i][j] = min(f[i - 1][j], f[i][j - 1]) + 1
                f[i][j] = min(f[i][j], f[i - 1][j - 1] + (word1[i] != word2[j]))

        return f[n][m]
# @lc code=end

