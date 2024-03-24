N, V = map(int, input().split())
# weight
w = [0] * (N + 5)
# value
v = [0] * (N + 5)
for i in range(1, N + 1):
    w[i], v[i] = map(int, input().split())

dp = [[0] * (V + 5) for _ in range(N + 5)]
for i in range(N + 1):
    for j in range(V + 1):
        if i == 0 or j == 0: continue
        if j >= w[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][V])
