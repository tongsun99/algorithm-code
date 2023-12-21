n, m = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0] * (n + 10)

# 前缀和
sum = 0
for i, num in enumerate(nums):
    sum += num
    sums[i] = sum

for i in range(m):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(sums[r] - sums[l - 1])
