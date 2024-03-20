n, k = map(int, input().split())
a = list(map(int, input().split()))
q = [0] * len(a)    # 维护可能的答案, 单调栈
hh = 0; tt = -1

mins = []
maxs = []

# find min
for i in range(len(a)):
    while hh <= tt and q[hh] <= i - k: hh += 1
    while hh <= tt and a[q[tt]] >= a[i]: tt -= 1
    tt += 1
    q[tt] = i
    if i >= k - 1: mins.append(a[q[hh]])    

# find max
hh = 0; tt = -1
for i in range(len(a)):
    while hh <= tt and q[hh] <= i - k: hh += 1
    while hh <= tt and a[q[tt]] <= a[i]: tt -= 1
    tt += 1
    q[tt] = i
    if i >= k - 1: maxs.append(a[q[hh]])    

for i in range(len(mins)):
    print(mins[i], end=" ")
print()
for i in range(len(maxs)):
    print(maxs[i], end=" ")
