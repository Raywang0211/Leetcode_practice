#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(nums,cur_list):
            if len(nums)==len(cur_list):
                res.append(cur_list[:])
                return 
            
            for num in nums:
                if num in cur_list:
                    continue
                cur_list.append(num)
                helper(nums,cur_list)
                cur_list.pop()

        helper(nums,[])
        return res

        
# @lc code=end

