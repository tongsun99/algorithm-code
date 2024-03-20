#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        r = []
        def dfs(s):
            if s == target:
                res.append(r.copy())
                return
            if s > target:
                return
            for i in range(n):
                if r and candidates[i] < r[-1]: continue
                r.append(candidates[i])
                dfs(s + candidates[i])
                r.pop()
        
        dfs(0)
        return res
            
# @lc code=end

