#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 所有字母:0的字典
        ht = {k:0 for k in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        hs = {k:0 for k in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        for char in t:
            ht[char] = ht[char] + 1
        j = 0
        cnt = 0
        res = ""
        for i in range(len(s)):
            hs[s[i]] += 1
            if hs[s[i]] <= ht[s[i]]:
                cnt += 1

            while j < i and hs[s[j]] > ht[s[j]]:
                hs[s[j]] -= 1
                j += 1

            if not res and cnt == len(t):
                res = s[j:i+1]
            if cnt == len(t) and i - j + 1 < len(res):
                res = s[j:i+1]
        return res


# @lc code=end
