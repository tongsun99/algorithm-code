n = float(input())
l = -10000
r = 10000
while (r - l > 1e-8):
    mid = (l + r) / 2
    if mid * mid * mid > n:
        r = mid
    else:
        l = mid
print(f'{l:.6f}')
