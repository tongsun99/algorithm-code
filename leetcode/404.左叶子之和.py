#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def is_leaf(node):
            if not node: return False
            return node.left == None and node.right == None
        
        def dfs(root):
            if not root: return
            if is_leaf(root.left): self.res += root.left.val
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return self.res
        
# @lc code=end

