#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        rs = []
        r = []

        def dfs(i):
            if i == n:
                rs.append(r.copy())
                return
            # put in
            r.append(nums[i])
            dfs(i+1)
            # not put in
            r.pop()
            dfs(i+1)

        dfs(0)
        return rs
# @lc code=end
