#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            p1 = self.get_len(s,i,i)
            p2 = self.get_len(s,i,i+1)
            ans = max([ans,p1,p2],key=len)
        return ans


    def get_len(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]
        
# @lc code=end

