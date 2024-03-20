# @before-stub-for-debug-begin
from python3problem139 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = 10000
        son = [[0] * 26 for _ in range(N)]
        is_word = [False] * N
        self.idx = 0
        
        def insert(word):
            p = 0
            for char in word:
                if son[p][ord(char) - ord('a')] == 0:
                    self.idx += 1
                    son[p][ord(char) - ord('a')] = self.idx
                p = son[p][ord(char) - ord('a')]
            is_word[p] = True
        
        for word in wordDict:
            word = word[::-1]
            insert(word)
        
        dp = [False] * len(s)
        
        for i in range(len(s)):
            j = i
            p = 0
            while j >= 0:
                if son[p][ord(s[j]) - ord('a')] == 0: break
                p = son[p][ord(s[j]) - ord('a')]
                if is_word[p]:
                    dp[i] = dp[i] or dp[j - 1]
                    if j == 0:
                        dp[i] = True
                j -= 1

        return dp[-1]

# @lc code=end

