n, q = map(int, input().split())
nums = list(map(int, input().split()))
for i in range(q):
    k = int(input())
    # 找起点
    l = 0; r = n - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < k: l = mid + 1
        else: r = mid
    st = l

    if nums[l] != k:
        print("-1 -1")
        continue

    # 找终点
    l = 0; r = n - 1
    while l < r:
        mid = (l + r + 1) // 2
        if nums[mid] > k: r = mid - 1
        else: l = mid
    ed = l
    print(f'{st} {ed}')
