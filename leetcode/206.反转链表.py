#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        if not a: return None
        b = a.next
        while b:
            c = b.next
            b.next = a
            a = b
            b = c
        head.next = None
        return a

    
        
# @lc code=end

