n, k = map(int, input().split())
nums = list(map(int, input().split()))


def solve(l, r, k):
    if l == r:
        return nums[l]
    i = l - 1
    j = r + 1
    mid = nums[(l+r)//2]
    while i < j:
        i += 1
        j -= 1
        while nums[i] < mid:
            i += 1
        while nums[j] > mid:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    sl = j - l + 1
    if sl < k: return solve(j + 1, r, k - sl)
    else: return solve(l, j, k)


print(solve(0, len(nums) - 1, k))
