#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 如果子树包含pq,返回最近公共祖先
        # 如果只包含p,返回p
        # 如果只包含q,返回q
        # 否则返回None
        if not root: return None
        if root == p: return p
        if root == q: return q
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l == None: return r
        if r == None: return l
        return root
# @lc code=end

