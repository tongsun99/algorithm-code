N = int(input())
nums = list(map(int, input().split()))
stack = []
for i in range(len(nums)):
    if len(stack) == 0:
        print("-1", end=" ")
    else:
        # 找到第一个比nums[i]小的数
        while len(stack) > 0 and stack[-1] >= nums[i]:
            res = stack.pop()
        if len(stack) == 0:
            print("-1", end=" ")
        else:
            print(f'{stack[-1]}', end=" ")
    stack.append(nums[i])
