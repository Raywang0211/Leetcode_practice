#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            i=0
            while (i+len(needle))<=len(haystack):
                if needle in haystack[i:i+len(needle)]:
                    return i
                else:
                    i+=1
                    continue
        else:
            return -1
        
# @lc code=end

