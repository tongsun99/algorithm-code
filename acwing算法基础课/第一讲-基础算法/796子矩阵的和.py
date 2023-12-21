N = 1010
a = [[0] * N for _ in range(N)]
s = [[0] * N for _ in range(N)]


if __name__ == '__main__':
    n, m, q = map(int, input().split())
    for i in range(n):
        a[i + 1] = [0] + list(map(int, input().split())) + a[m+1:]
        
    # cal s
    for row in range(1, n + 1, 1):
        for col in range(1, m + 1, 1):
            s[row][col] = s[row - 1][col] + s[row][col - 1] - s[row - 1][col - 1] + a[row][col]
            
    for i in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        print(s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1])
        