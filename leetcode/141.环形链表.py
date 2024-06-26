#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        if not head.next: return False
        fast = head.next
        slow = head
        while fast and slow:
            if fast == slow: return True
            if not fast.next: return False 
            fast = fast.next.next
            slow = slow.next
        return False
        
# @lc code=end

