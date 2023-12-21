def big_add(a_list, b_list):
    if len(b_list) > len(a_list): return big_add(b_list, a_list)
    t = 0
    for i in range(len(a_list)):
        t += a_list[i]
        if i < len(b_list): t += b_list[i]
        c_list.append(t % 10)
        t //= 10
    
    if t: c_list.append(t)
    return c_list
    
if __name__ == "__main__":
    a = input(); b = input()
    a_list = []; b_list = []; c_list = []
    for i in range(len(a) - 1, -1, -1):
        a_list.append(int(a[i]))
        
    for i in range(len(b) - 1, -1, -1):
        b_list.append(int(b[i]))
    
    c_list = big_add(a_list, b_list)
    for i in range(len(c_list) - 1, -1, -1):
        print(c_list[i], end="")
