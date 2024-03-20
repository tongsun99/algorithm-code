#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        res = []
        st = intervals[0][0]
        ed = intervals[0][1]
        for i, [a, b] in enumerate(intervals):
            if i == 0:
                continue
            if a <= ed:
                ed = max(ed, b)
            else:
                res.append([st, ed])
                st = a
                ed = b
        res.append([st, ed])
        return res


# @lc code=end
