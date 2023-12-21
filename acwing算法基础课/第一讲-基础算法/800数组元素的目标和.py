n, m, x = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
i = 0
j = m - 1
while i < n and j >= 0:
    if A[i] + B[j] == x:
        break
    elif A[i] + B[j] > x:
        j -= 1
    else:
        i += 1

print(f'{i} {j}')
