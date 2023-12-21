n, m = map(int, input().split())

adds = []
idxs = []
queries = []
a = [0] * (n + 2 * m + 10)
s = [0] * (n + 2 * m + 10)

for i in range(n):
    x, c = map(int, input().split())
    adds.append((x, c))
    idxs.append(x)

for i in range(m):
    l, r = map(int, input().split())
    queries.append((l, r))
    idxs.append(l)
    idxs.append(r)

idxs = sorted(list(set(idxs)))


def find(fidx):
    # 找到第一个大于等于fidx的下标
    l = 0
    r = len(idxs) - 1
    while l < r:
        mid = (l + r) // 2
        if idxs[mid] >= fidx:
            r = mid
        else:
            l = mid + 1
    return l + 1


for (x, c) in adds:
    a[find(x)] += c

for i in range(1, n + 2 * m + 1):
    s[i] = s[i - 1] + a[i]


for (l, r) in queries:
    print(s[find(r)] - s[find(l) - 1])
