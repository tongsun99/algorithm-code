#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0: return []
        dial = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []
        r = []
        def dfs(i):
            if i == n:
                res.append("".join(r))
                return
            
            for c in dial[digits[i]]:
                r.append(c)
                dfs(i + 1)
                r.pop()
        
        dfs(0)
        return res
# @lc code=end

