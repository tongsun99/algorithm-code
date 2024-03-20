# @before-stub-for-debug-begin
from python3problem131 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        def check(s):
            if len(s) == 0:
                return False
            i = 0
            j = len(s) - 1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        res = []
        r = []

        def dfs(step):
            if step == n:
                res.append(r.copy())
                return

            for i in range(step+1, n+1):
                if check(s[step:i]):
                    r.append(s[step:i])
                    dfs(i)
                    r.pop()

        dfs(0)
        return res
# @lc code=end
