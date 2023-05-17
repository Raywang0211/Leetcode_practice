#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
            
        if not head or not head.next: return head

        p = head
        new_start = p.next

        while True:
            q = p.next
            temp = q.next #p.next.next
            q.next = p
            if not temp or not temp.next:
                p.next = temp
                break
            p.next = temp.next
            p = temp
        return new_start 

                  
        
# @lc code=end

