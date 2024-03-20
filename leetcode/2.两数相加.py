#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy, p1, p2 = ListNode(), l1, l2
        p = dummy
        add = 0
        c = 0
        while p1 or p2:
            if p1: add += p1.val
            if p2: add += p2.val
            if c: add += c
            c = add // 10
            add %= 10
            p.next = ListNode(add)
            if p1: p1 = p1.next
            if p2: p2 = p2.next
            p = p.next
            add = 0
        if c == 1: p.next = ListNode(1)
            
        return dummy.next
            
            
# @lc code=end

