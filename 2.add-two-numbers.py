#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        N1=N2=""
        while l1:
            N1+=str(l1.val)
            l1=l1.next
        while l2:
            N2+=str(l2.val)
            l2=l2.next
    
        N3 = str(int(N1[::-1]) + int(N2[::-1]))[::-1]
        ans =n = ListNode(0)
        for i in N3:
            ans.next = ListNode(i)
            ans = ans.next
        return n.next
        
# @lc code=end

