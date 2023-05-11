#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        top = 0
        ans = pow(10,5)+1
        total_sum = 0
        for i in range(1,len(nums)+1):
            total_sum+=nums[i-1]
            while (total_sum>=target):
                if ans>i-top:
                    ans = i-top
                total_sum-=nums[top]
                top+=1
        if ans==pow(10,5)+1:
            return 0
        return ans

        
# @lc code=end

