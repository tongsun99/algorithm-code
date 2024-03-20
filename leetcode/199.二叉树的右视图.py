#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append((root, 1))
        res = []
        while q:
            top, level = q[0]
            if level > len(res):
                res.append([])

            res[-1].append(top.val)

            q.popleft()

            if top.left:
                q.append((top.left, level + 1))
            if top.right:
                q.append((top.right, level + 1))
        ret = [level[-1] for level in res]

        return ret

# @lc code=end
