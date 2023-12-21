def big_div(A_list, b):
    c_list = []; r = 0
    for i in range(len(A_list) - 1, -1, -1):
        r = r * 10 + A_list[i]
        c_list.append(r // b)
        r %= b
    
    c_list.reverse()
    
    # 去除前导0
    while (len(c_list) > 1 and c_list[-1] == 0): c_list.pop()
    return c_list, r
    
if __name__ == '__main__':
    A = input()
    b = int(input())
    A_list = []
    for char in reversed(A):
        A_list.append(int(char))
    
    c_list, r = big_div(A_list, b)
    for ele in reversed(c_list):
        print(ele, end="")
    print('\n', end="")
    print(r)