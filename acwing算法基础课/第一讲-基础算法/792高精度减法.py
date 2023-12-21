def cmp(a_list, b_list):
    if len(a_list) != len(b_list): return len(a_list) > len(b_list)
    else:
        for i in range(len(a_list) - 1, -1, -1):
            if a_list[i] != b_list[i]: return a_list[i] > b_list[i]
    return True

def big_sub(a_list, b_list):
	c_list = []
	t = 0
	for i in range(len(a_list)):
		t = a_list[i] - t
		if i < len(b_list): t -= b_list[i]
		c_list.append((t + 10) % 10)
		if t < 0: t = 1
		else: t = 0
	# 去除前导0
	while (len(c_list) > 1 and c_list[-1] == 0): c_list.pop() 
	return c_list
    
    
if __name__ == "__main__":
    a = input(); b = input()
    a_list = []; b_list = []
    for i in range(len(a) - 1, -1, -1):
        a_list.append(int(a[i]))
        
    for i in range(len(b) - 1, -1, -1):
        b_list.append(int(b[i]))
    
    if cmp(a_list, b_list):
        c_list = big_sub(a_list, b_list)
        for i in range(len(c_list) - 1, -1, -1):
            print(c_list[i], end="")
    else:
        c_list = big_sub(b_list, a_list)
        print("-", end="")
        for i in range(len(c_list) - 1, -1, -1):
            print(c_list[i], end="")
        