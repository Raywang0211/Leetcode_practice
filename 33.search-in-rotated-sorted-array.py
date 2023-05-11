#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minn =10**4
        for i in nums:
            if i<minn:
                minn=i
            else:
                continue
        new_list = nums[nums.index(minn):]+nums[0:nums.index(minn)]

        upper = len(new_list)-1
        lower = 0

        while lower<=upper:
            mid = (upper+lower)//2
            if new_list[mid]>target:
                upper = mid-1
            elif new_list[mid]<target:
                lower = mid+1
            else:
                return nums.index(new_list[mid]) 
        return -1



        
# @lc code=end

