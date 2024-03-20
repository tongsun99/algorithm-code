#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.res = 0

        def dfs(root):
            if not root:
                return False
            if dfs(root.left):
                return True

            self.cnt += 1
            if self.cnt == k:
                self.res = root.val
                return True

            if dfs(root.right):
                return True
        dfs(root)

        return self.res
# @lc code=end
