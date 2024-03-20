#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.ans = 0
        def dfs(root):
            if not root:
                return 0
            l_depth = dfs(root.left)
            r_depth = dfs(root.right)
            self.ans = max(self.ans, l_depth + r_depth)
            return max(l_depth, r_depth) + 1

        dfs(root)
        return self.ans
# @lc code=end
