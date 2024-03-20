#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
    
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def compare(hash_table_1, hash_table_2):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if hash_table_1[c] != hash_table_2[c]:
                    return False
            return True

        hash_table_p = {c: 0 for c in "abcdefghijklmnopqrstuvwxyz"}
        hash_table_s = {c: 0 for c in "abcdefghijklmnopqrstuvwxyz"}
        # build hash_table
        for c in p:
            hash_table_p[c] += 1
        for c in s[0:len(p)]:
            hash_table_s[c] += 1

        i = 0
        res = []
        while True:
            if compare(hash_table_s, hash_table_p):
                res.append(i)
            if i + 1 > len(s) - len(p):
                break
            hash_table_s[s[i]] -= 1
            hash_table_s[s[i + len(p)]] += 1
            i += 1

        return res
# @lc code=end
