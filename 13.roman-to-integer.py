#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        extranumber = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        singlenumber = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        final_number = 0
        flag = 1
        for id in range(len(s)):
            if flag:
                if s[id:id+2] in extranumber:
                    final_number+=extranumber[s[id:id+2]]
                    flag=0
                else:
                    final_number+=singlenumber[s[id]]
            else:
                flag=1
                continue
        return final_number

        
# @lc code=end

