#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and slow:
            if not fast.next: return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow: break
        if not (fast and slow): return None
        p = head
        while p and fast:
            if p == fast: return p
            p = p.next
            fast = fast.next
        return None
        
        
            
        
# @lc code=end

