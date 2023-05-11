#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0

        for i in range(0,len(s)):
            j=0
            while j<=len(s)-i-1:
                s1 = s[j:j+i+1]
                repeat = 0
                for k in range(len(s1)):
                    if s1[k] in s1[k+1:]:
                        repeat = 1
                        break
                    else:
                        continue
                if repeat==0:
                    max_len=i+1
                else:
                    pass
                j+=1
        return max_len


        
# @lc code=end

