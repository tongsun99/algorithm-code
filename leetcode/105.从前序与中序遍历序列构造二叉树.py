#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        # hash
        pos = {}
        for i in range(n):
            pos[inorder[i]] = i

        def build(pl, pr, il, ir):
            if pl > pr or il > ir:
                return None
            root = TreeNode(preorder[pl])
            k = pos[root.val]
            root.left = build(pl+1, pl+1+k-1-il, il, k-1)
            root.right = build(pl+1+k-1-il+1, pl+1+k-1-il+1+ir-k-1, k+1, ir)
            return root
        return build(0, n - 1, 0, n - 1)
# @lc code=end
