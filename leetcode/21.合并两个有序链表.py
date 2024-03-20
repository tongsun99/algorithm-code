#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy, h1, h2 = ListNode(), list1, list2
        p = dummy
        while h1 and h2:
            if h1.val <= h2.val:
                p.next = h1
                p = p.next
                h1 = h1.next
            else:
                p.next = h2
                p = p.next
                h2 = h2.next
        if h1: p.next = h1
        else: p.next = h2
        return dummy.next
# @lc code=end

