def big_mul(a_list, b):
    c_list = []
    t = 0; i = 0
    while i < len(a_list):
        if i < len(a_list): t += a_list[i] * b
        c_list.append(t % 10)
        t = t // 10
        i += 1
    c_list.append(t)

    # 去除前导0
    while (len(c_list) > 1 and c_list[-1] == 0): c_list.pop()
    return c_list

if __name__ == '__main__':
    a = input()
    b = int(input())
    a_list = []
    for char in reversed(a):
        a_list.append(int(char))
    c_list = big_mul(a_list, b)
    for i in range(len(c_list) - 1, -1, -1):
        print(c_list[i], end="")
