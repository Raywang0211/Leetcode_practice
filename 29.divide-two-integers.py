#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend>0 and divisor<0) or (dividend<=0 and divisor>0):
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = len(range(0,dividend-divisor+1,divisor))


        if sign==-1:
            result = -result
        max_range = (2**31)-1
        min_range = -(2**31)
        ans = min(max(min_range,result),max_range)
        return ans
# @lc code=end

