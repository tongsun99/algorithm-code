N = 1010
a = [[0] * N for _ in range(N)]
b = [[0] * N for _ in range(N)]
def insert(x1, y1, x2, y2, c):
    b[x1][y1] += c
    b[x2 + 1][y1] -= c
    b[x1][y2 + 1] -= c
    b[x2 + 1][y2 + 1] += c
    
if __name__ == '__main__':
    n, m, q = map(int,input().split())
    for i in range(n):
        a[i + 1] = [0] + list(map(int, input().split())) + a[m + 1:]
        for col in range(1, m + 1):
            insert(i + 1, col, i + 1, col, a[i + 1][col])
            
    for _ in range(q):
        x1, y1, x2, y2, c = map(int, input().split())
        insert(x1, y1, x2, y2, c)
    
    
    for row in range(1, n + 1):
        for col in range(1, m + 1):
            a[row][col] = a[row - 1][col] + a[row][col - 1] - a[row - 1][col - 1] + b[row][col]    
            print(a[row][col], end=" ")
        print("")