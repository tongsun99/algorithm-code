#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, num in enumerate(nums):
            if str(target - num) in hash_table.keys():
                return [hash_table[str(target-num)], i]
            else:
                hash_table[str(num)] = i
# @lc code=end
