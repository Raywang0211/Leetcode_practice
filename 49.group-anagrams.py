#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        if len(strs)<1:
            return strs
        else:
            for i in range(len(strs)):
                temp = "".join(sorted(strs[i]))
                if temp in ans.keys():
                    ans[temp].append(strs[i])
                else:
                    ans[temp] = [strs[i]]
        return ans.values()

# @lc code=end
