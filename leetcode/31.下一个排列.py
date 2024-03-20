#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1, 3, 5, 4, 1
        n = len(nums)
        # find 3
        i = n - 1
        while i >= 1:
            if nums[i] > nums[i - 1]: break
            i -= 1
        if i == 0:
            print("here")
            nums.reverse()
            return
        print(i)
        # find 4
        i_1 = i - 1
        i = n - 1
        while i > i_1 and nums[i] <= nums[i_1]:
            i -= 1
        print(f'swap i: {i}, i_1: {i_1}')
        # swap
        nums[i], nums[i_1] = nums[i_1], nums[i]
        # reverse
        part = nums[i_1 + 1:]
        part.reverse()
        nums[i_1+1:] = part
# @lc code=end

