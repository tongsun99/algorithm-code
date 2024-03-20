#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        path = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            path.append(root.val)
            helper(root.right)
        helper(root)

        for i in range(1, len(path)):
            if path[i] <= path[i - 1]:
                return False
        return True
# @lc code=end
