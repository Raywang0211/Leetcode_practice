#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for id1,a in enumerate(nums):
            t2 = target - a
            if t2 in nums:
                id2 = nums.index(t2)
                if id2==id1:
                    continue
                else:
                    return id1,id2
            else:
                continue

        
# @lc code=end

