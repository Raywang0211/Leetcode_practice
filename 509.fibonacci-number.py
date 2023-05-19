#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        cash = dict()

        if n<2:
            return n
        if n in cash.keys():
            return cash[n]
        result = self.fib(n-1)+self.fib(n-2)
        cash[n] = result
        return result
        
# @lc code=end

