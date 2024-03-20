#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sums = []
        for i in range(len(nums)):
            if i == 0: sums.append(nums[i])
            else: sums.append(sums[-1] + nums[i])
        if sums[-1] < target: return 0
        j = 0
        res = len(nums) + 10
        for i in range(len(nums)):
            if sums[i] < target: continue
            res = min(res, i + 1)
            while j <= i:
                if sums[i] - sums[j] >= target:
                    j += 1 
                    res = min(res, i - j + 1)
                else:
                    break
        return res
             
            
# @lc code=end

