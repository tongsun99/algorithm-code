#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}
        for str in strs:
            k = "".join(sorted(str))
            if k in hash_table.keys():
                hash_table[k].append(str)
            else:
                hash_table[k] = [str]
        res = []
        for k, v in hash_table.items():
            res.append(v)
        return res

# @lc code=end
