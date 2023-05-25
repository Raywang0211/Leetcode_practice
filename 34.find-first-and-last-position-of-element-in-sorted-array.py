#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low_index = -1
        high_index = -1

        for i in range(len(nums)):
            if nums[i]==target:
                low_index=i
                break
            else:
                continue
        for i in range(-1,-len(nums)-1,-1):
            if nums[i] ==target:
                high_index=len(nums)+i
                break
            else:
                continue
        if low_index==-1 or high_index==-1:
            return [-1,-1]
        else:
            return [low_index,high_index]
             

        
# @lc code=end

