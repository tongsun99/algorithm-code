n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = False
j = 0
i = 0
while i < n:
    while j < m and a[i] != b[j]:
        j += 1
    if j >= m:
        break
    j += 1

    i += 1
res = (i == n)

if res:
    print("Yes")
else:
    print("No")
