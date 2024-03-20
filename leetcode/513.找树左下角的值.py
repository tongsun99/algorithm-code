#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 1))
        res = []
        while q:
            top, level = q.popleft()
            if level > len(res):
                res.append([])
            res[-1].append(top.val)

            if top.left:
                q.append((top.left, level+1))
            if top.right:
                q.append((top.right, level+1))
        return res[-1][0]
# @lc code=end
