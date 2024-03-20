#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA; pB = headB
        # 计算长度
        lenA = 0; lenB = 0
        while pA:
            lenA += 1
            pA = pA.next
        while pB:
            lenB += 1
            pB = pB.next
        pA = headA; pB = headB
        # 长的先走
        if lenA > lenB:
            i = 0
            while pA and i < lenA - lenB:
                pA = pA.next
                i += 1
        else:
            i = 0
            while pB and i < lenB - lenA:
                pB = pB.next
                i += 1
        # 一起走
        while pA or pB:
            if pA == pB: return pA
            else:
                pA = pA.next
                pB = pB.next
        return None
        
# @lc code=end

