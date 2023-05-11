#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            x=str(x)  
            x1 = x[0:int(len(x)/2)][::-1]
            if (len(str(x))%2):
                x2 = x[int(len(x)/2)+1:]
            else:
                x2 = x[int(len(x)/2):]
            if x1==x2:
                return True
            else:
                return False

        
# @lc code=end

