#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.res = 0
        if not root: return 0
        root.sums = [root.val]
        def dfs(root):
            if not root: return
            for s in root.sums:
                if s == targetSum: self.res += 1
            if root.left:
                root.left.sums = [root.left.val] + [(s + root.left.val) for s in root.sums]
            dfs(root.left)
            if root.right:
                root.right.sums = [root.right.val] + [(s + root.right.val) for s in root.sums]
            dfs(root.right)
        
        dfs(root)
        return self.res
# @lc code=end

