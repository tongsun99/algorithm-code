n = int(input())
intervals = []
for i in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r))

intervals.sort(key=lambda a: a[0])

cnt = 0
last_end = float("-inf")
for i, (l, r) in enumerate(intervals):
    if l > last_end:
        cnt += 1
    last_end = max(last_end, r)

print(cnt)
