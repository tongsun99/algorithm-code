#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hash_table = {}
        j = 0
        res = 0
        for i in range(n):
            if s[i] in hash_table.keys():
                hash_table[s[i]] += 1
            else:
                hash_table[s[i]] = 1
            while (j < i and hash_table[s[i]] == 2):
                hash_table[s[j]] -= 1
                j += 1
            res = max(res, i - j + 1)
        return res


# @lc code=end
