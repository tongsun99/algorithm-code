#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # LDR
        nums = []
        def dfs(root):
            if not root: return
            dfs(root.left)
            nums.append(root.val)
            dfs(root.right)
        dfs(root)
        min_val = nums[1] - nums[0]
        for i in range(1, len(nums)):
            min_val = min(min_val, nums[i] - nums[i - 1])
        return min_val
# @lc code=end

