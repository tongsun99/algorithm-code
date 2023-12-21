n = int(input())
nums = list(map(int, input().split()))
res = 1
cnt = [0] * 100010

j = 0
for i in range(n):
    cnt[nums[i]] += 1
    while (j <= i and cnt[nums[i]] == 2):
        cnt[nums[j]] -= 1
        j += 1
    res = max(res, i - j + 1)

print(res)
