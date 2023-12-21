def quick_sort(l, r):
    if l >= r: return
    i = l - 1
    j = r + 1
    while i < j:
        i += 1
        j -= 1
        if nums[i] > nums[j]: nums[i], nums[j] = nums[j], nums[i]
        for num in nums: print(num, end=" ")
        
    quick_sort(l, i)
    quick_sort(i + 1, r)

n = int(input())
nums = list(map(int, input().split()))
quick_sort(0, len(nums) - 1)

for num in nums: print(num, end=" ")