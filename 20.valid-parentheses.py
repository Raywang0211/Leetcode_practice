#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {")":"(",
                "]":"[",
                "}":"{"}
        stack = []

        for char in s:
            if char in lookup.values():
                stack.append(char)
            elif stack and stack[-1]==lookup[char]:
                stack.pop()
            else:
                return False

        return stack==[] 


        
# @lc code=end

