#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        tmp_root = root
        while root:
            if root.left:
                tmp_l = root.left
                tmp_r = root.right
                # 左子树的最右边的点
                while tmp_l.right:
                    tmp_l = tmp_l.right
                root.right = root.left
                tmp_l.right = tmp_r
            root.left = None
            root = root.right

        return tmp_root
                               
# @lc code=end

