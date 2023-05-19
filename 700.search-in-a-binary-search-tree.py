#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #base
        if root == None: return None
        if root.val == val:   
            return root
        

        #relation
        if root.val < val:
            return self.searchBST(root.right,val)
        else:
            return self.searchBST(root.left,val)
             
# @lc code=end

