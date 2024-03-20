#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = []
        p = head
        while p:
            tmp.append(p.val)
            p = p.next
        i = 0; j = len(tmp) - 1
        while i < j:
            if tmp[i] != tmp[j]: return False
            else:
                i += 1
                j -= 1
        return True
# @lc code=end

