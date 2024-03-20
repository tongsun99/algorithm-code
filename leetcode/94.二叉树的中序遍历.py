#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        # 0 left 0 right 0
        # 1 left 1 right 0
        # 2 left 1 right 1
        stack.append((root, 0))
        while stack:
            root, flag = stack[-1]
            if not root: 
                stack.pop()
                continue
            if flag == 0:
                stack[-1] = (root, 1)
                stack.append((root.left, 0))
            elif flag == 1:
                res.append(root.val)
                stack[-1] = (root, 2)
                stack.append((root.right, 0))
            elif flag == 2:
                stack.pop()
        return res 
# @lc code=end

