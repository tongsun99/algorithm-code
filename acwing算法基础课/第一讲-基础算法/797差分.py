n, m = map(int, input().split())
nums = list(map(int, input().split()))
b = [0] * (n + 10)
a = [0] * (n + 10)


def insert(l, r, c):
    b[l] += c
    b[r + 1] -= c


for i, num in enumerate(nums):
    insert(i, i, num)

for i in range(m):
    l, r, c = map(int, input().split())
    insert(l - 1, r - 1, c)

sum = 0
for i in range(n):
    sum += b[i]
    print(sum, end=" ")
