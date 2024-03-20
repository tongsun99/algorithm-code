#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        r = []
        def dfs(step, stack):
            if step == 2 * n:
                if not stack:
                    res.append("".join(r.copy()))
                return

            for c in ["(", ")"]:
                r.append(c)
                tmp = stack.copy()
                # pop stack
                if stack and stack[-1] == "(" and c == ")":
                    stack.pop()
                else:
                    stack.append(c)
                
                dfs(step + 1, stack)
                stack = tmp
                r.pop()
        dfs(0, [])
        return res
# @lc code=end

