#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        g = [[0] * (numCourses + 5) for _ in range(numCourses + 5)]
        for c1, c2 in prerequisites:
            g[c1][c2] = 1
            indegrees[c2] += 1
        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0: q.append(i)
        
        while q:
            top = q.popleft()
            for i in range(numCourses):
                if g[top][i] == 1:
                    g[top][i] = 0
                    indegrees[i] -= 1
                    if indegrees[i] == 0: q.append(i)

        if sum(indegrees) > 0: return False
        return True

# @lc code=end

