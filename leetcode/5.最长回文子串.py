#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        chars = [char for char in s]
        s = "#".join(chars)
        res = ""
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            cur = s[left + 1: right - 1 + 1]
            # remove # 
            cur_ = []
            for char in cur:
                if char == '#': continue
                cur_ += char
            cur_s = "".join(cur_)
            if len(cur_s) > len(res): res = cur_s
        return res
            


# @lc code=end
