#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_sort(nums, 0, len(nums) - 1, k)

    
    def quick_sort(self, nums, l, r, k):
        if l >= r: return nums[l]
        i = l - 1; j = r + 1
        mid = nums[(l + r) // 2]
        while i < j:
            i += 1
            j -= 1
            while nums[i] < mid: i += 1
            while nums[j] > mid: j -= 1
            if i < j: nums[i], nums[j] = nums[j], nums[i]
        if r - j >= k: return self.quick_sort(nums, j + 1, r, k)
        else: return self.quick_sort(nums, l, j, k - r + j)
# @lc code=end

