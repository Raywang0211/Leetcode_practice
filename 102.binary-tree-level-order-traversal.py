#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = dict()
        def bfs(root,level):
            if not root: return
            if level in d.keys():
                d[level].append(root.val)
            else:
                d[level] = [root.val]
            bfs(root.left,level+1)
            bfs(root.right,level+1)
        
        bfs(root,0)
        return d.values()


        
# @lc code=end

