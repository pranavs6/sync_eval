for _ in range(int(input())):
    res = ''
    input_val = str(input())
    if '10' in input_val:
        ten_ind = input_val.index('10')
        exp_val = input_val[ten_ind + 2 :]
        ev = int(exp_val)
        if len(str(int(exp_val)))==len(exp_val) and ev>=2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

