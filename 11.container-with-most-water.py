#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_pointer = 0
        r_pointer = len(height)-1
        max_water = 0

        while l_pointer <= r_pointer:
            max_water = max(max_water,(min(height[r_pointer],height[l_pointer])*(r_pointer-l_pointer)))
            if height[l_pointer]>=height[r_pointer]:
                r_pointer=r_pointer-1
            else:
                l_pointer=l_pointer+1
        return max_water

        
        
# @lc code=end

