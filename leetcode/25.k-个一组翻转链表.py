#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        # 后面有没有k个元素
        while True:
            i = 0
            q = pre
            while i < k:
                q = q.next
                if not q: break
                i += 1
            if i < k: return dummy.next
            a = pre.next
            b = a.next
            for i in range(k - 1):
                c = b.next
                b.next = a
                a = b
                b = c
            c = pre.next
            pre.next = a
            c.next = b
            pre = c
# @lc code=end

