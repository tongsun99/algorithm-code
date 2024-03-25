n, m = map(int, input().split())
p = list(range(0, n+1))

def find(x):
    if p[x] != x: p[x] = find(p[x])
    return p[x]
    
for i in range(m):
    op, a, b = input().split()
    a = int(a)
    b = int(b)
    if op == "M":
        p[find(a)] = find(b)
    elif op == "Q":
        if find(a) == find(b):
            print("Yes")
        else:
            print("No")
