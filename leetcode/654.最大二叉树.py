#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def build(l, r):
            if l > r: return None
            # find max
            max_val = -1
            max_idx = l
            for i in range(l, r + 1):
                if nums[i] > max_val:
                    max_val = nums[i]
                    max_idx = i
            
            root = TreeNode(max_val)
            root.left = build(l, max_idx - 1)
            root.right = build(max_idx + 1, r)
            return root

        return build(0, len(nums) - 1)
            
# @lc code=end
