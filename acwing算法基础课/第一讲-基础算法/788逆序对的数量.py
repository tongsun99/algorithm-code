n = int(input())
nums = list(map(int, input().split()))
tmp = [0] * (n + 10)

def merge_sort(l, r):
    # 逆序对是比较大小得到的 -> 想到排序
    # 分治 -> 归并排序
    if l >= r: return 0
    mid = (l + r) // 2
    res = merge_sort(l, mid) + merge_sort(mid + 1, r)
    i = l
    j = mid + 1
    k = 0
    while i <= mid and j <= r:
        if nums[i] <= nums[j]: tmp[k] = nums[i]; i += 1; k += 1
        else: tmp[k] = nums[j]; j += 1; k += 1; res += mid - i + 1
    
    while i <= mid: tmp[k] = nums[i]; i += 1; k += 1
    while j <= r: tmp[k] = nums[j]; j += 1; k += 1

    for i in range(k): nums[l+i] = tmp[i]
    
    return res

res = merge_sort(0, n - 1)
print(res)
