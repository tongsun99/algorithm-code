def qmi(a, k, p):
    res = 1
    while k:
        if k & 1:
            res = res * a % p
        a = a * a % p
        k >>= 1
    return res % p

n = int(input())
for i in range(n):
    a, b, p = map(int, input().split())
    print(qmi(a, b, p))


    